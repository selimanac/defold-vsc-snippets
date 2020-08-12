![Defold Api](https://selimanac.github.io/assets/gfx/vscode-api-2000x666.png)

# Defold API Snippets for Visual Studio Code

Full api snippets for [Defold Engine](https://www.defold.com/) is available on [marketplace](https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets).  
All Lua and C++ methods, messages,  properties and brief descriptions are included.

**Marketplace:** https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets  
**Github:** https://github.com/selimanac/defold-vsc-snippets

------------

![vcs](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/vcs.png)


### Ordered Tabstops

![Ordered Tabstops](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/orderedtabstops.gif)

### Message Generation



`play_sound` ->  `msg.post(receiver, "play_sound", {[delay], [gain]})`

`model_animation_done` -> `msg.post(receiver, "model_animation_done", {animation_id, playback})`

![focus](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/input_focus.gif)

![focus](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/clear_color.gif)

### Properties with quotation marks

`"scale"`

## Release Notes

### 1.2.171
* API version 1.2.171
* Version numbering has changed for better following the Defold API changes.

### 1.2.2
* API version 1.2.169
* Python script is updated. It is now download, unpack and parse the docs. Python script requires Python version 2.7. It may fail with Python version 3.x

### 1.2.1
* API version 1.2.163

### 1.2.0

LUA and C++ (Defold SDK) APIs are separated. You can use Defold SDK snippets with C++ now.

### 1.1.7
* API version 1.2.156

### 1.1.6
* API version 1.2.149

### 1.1.5
* API version 1.2.147


### 1.1.4

* API version 1.2.138
* Missing functions, methods and properties are added properly.
* Properties added to the body.

(Sorry for the version numbering, vsce publish minor cause this )



### 1.0.2

* Missing functions, methods and properties are added.
* Args added to the list.

### 1.0.0

* Initial release based on API version 1.2.137. 

## Recommended Settings & Extension

### Add .script files to your settings

```json
"files.associations": {
        "*.script": "lua",
        "*.gui_script": "lua",
        "*.render_script": "lua",
        "*.editor_script": "lua"
      }
```  

### Useful Extensions

* [EmmyLua](https://marketplace.visualstudio.com/items?itemName=tangzx.emmylua) (Suggested)
* [Lua language support for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=keyring.Lua)
* [Lint Lua scripts with luac or luajit](https://marketplace.visualstudio.com/items?itemName=dcr30.lualinter)
* [Improved Lua syntax highlighting](https://marketplace.visualstudio.com/items?itemName=jep-a.lua-plus)
* [Support go to defintion and List Document Symbols.](https://marketplace.visualstudio.com/items?itemName=xxxg0001.lua-for-vscode)
* [Intellisense and Linting for Lua](https://marketplace.visualstudio.com/items?itemName=trixnz.vscode-lua)


## Json Parser

I build this snippets by using a simple Python script. It parses all json files from api docs and converts them to single snippet file. It is available in the `src` folder of [Github repo](https://github.com/selimanac/defold-vsc-snippets).
