from krita import *
from PyQt5.QtCore import QStandardPaths
import os
import shutil

class LayerVisibilitySwitchExtension(Extension):

    def __init__(self, parent):
        super().__init__(parent)
        self.plugin_dir = os.path.dirname(__file__)
        self.action_file_name = "layer_visibility_switch.action"

    def setup(self):
        # Install the .action file on first run for automatic shortcut registration
        self.install_action_file()

    def createActions(self, window):
        # Create actions in the Tools -> Scripts menu
        self.action_up = window.createAction("layer_vis_up", "Switch Visibility Up", "tools/scripts")
        self.action_up.triggered.connect(self.switch_up)

        self.action_down = window.createAction("layer_vis_down", "Switch Visibility Down", "tools/scripts")
        self.action_down.triggered.connect(self.switch_down)

    def install_action_file(self):
        """Copies the .action file to the Krita resources directory automatically."""
        try:
            # Determine the writable Krita resources directory
            data_location = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
            resources_dir = os.path.join(data_location, "krita")
            actions_dir = os.path.join(resources_dir, "actions")
            os.makedirs(actions_dir, exist_ok=True)

            # Source: the .action file shipped inside the plugin folder
            src = os.path.join(self.plugin_dir, self.action_file_name)
            dst = os.path.join(actions_dir, self.action_file_name)

            if not os.path.exists(dst):
                if os.path.exists(src):
                    shutil.copyfile(src, dst)
                    print(f"Layer Visibility Switch: Keyboard shortcut file installed to {dst}. Please restart Krita to use it.")
                else:
                    print(f"Layer Visibility Switch: Source action file not found at {src}")
        except Exception as e:
            print(f"Layer Visibility Switch: Could not install .action file: {e}")

    def switch_up(self):
        doc = Krita.instance().activeDocument()
        if not doc:
            return

        active = doc.activeNode()
        if not active:
            return

        parent = active.parentNode()
        if not parent:
            return

        children = parent.childNodes()
        try:
            idx = children.index(active)
            if idx + 1 < len(children):
                # Hide current
                active.setVisible(False)
                active.setBlendingMode(active.blendingMode())

                # Move to next (which is "Up" in the user's perception)
                next_node = children[idx + 1]
                doc.setActiveNode(next_node)
                next_node.setVisible(True)
                next_node.setBlendingMode(next_node.blendingMode())
        except ValueError:
            pass

    def switch_down(self):
        doc = Krita.instance().activeDocument()
        if not doc:
            return

        active = doc.activeNode()
        if not active:
            return

        parent = active.parentNode()
        if not parent:
            return

        children = parent.childNodes()
        try:
            idx = children.index(active)
            if idx > 0:
                # Hide current
                active.setVisible(False)
                active.setBlendingMode(active.blendingMode())

                # Move to previous (which is "Down" in the user's perception)
                prev_node = children[idx - 1]
                doc.setActiveNode(prev_node)
                prev_node.setVisible(True)
                prev_node.setBlendingMode(prev_node.blendingMode())
        except ValueError:
            pass
