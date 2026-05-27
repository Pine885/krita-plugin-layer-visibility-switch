# Layer Visibility Switch

A simple Krita plugin that allows you to navigate your layer stack while automatically toggling visibility.

## 🚀 What it does
This plugin implements a "Solo" navigation mode for your layers. When you move the active layer focus up or down:
- The **previous** active layer is automatically set to **invisible**.
- The **new** active layer is automatically set to **visible**.

This is ideal for quickly cycling through layers to see their individual contributions without manually clicking the visibility eye icon for each one.

![][switchvisibilitylayer.gif](https://github.com/Pine885/krita-plugin-layer-visibility-switch/blob/main/switchvisibilitylayer.gif)

## 📂 Installation
1. In Krita, go to **Tools** $\rightarrow$ **Scripts** $\rightarrow$ **Import Python Plugin from File...**
2. Select the `layer-visibility-switch.zip` file.
3. Restart **Krita**.
4. Go to **Settings** $\rightarrow$ **Configure Krita** $\rightarrow$ **Python Plugin Manager**.
5. Find **Layer Visibility Switch** in the list, check the box to enable it, and click **OK**.
6. Restart **Krita** one more time.

## ⌨️ Setting Keyboard Shortcuts
The plugin automatically installs its action definitions. To assign keys:
1. Go to **Settings** $\rightarrow$ **Configure Krita** $\rightarrow$ **Keyboard Shortcuts**.
2. Search for **"Layer Visibility Switch"**.
3. Assign your preferred keys to **Switch Visibility Up** and **Switch Visibility Down**.
