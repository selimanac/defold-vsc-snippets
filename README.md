![Defold API Reference](https://selimanac.github.io/assets/gfx/vscode-api-2000x666.png)

# Defold API Snippets for Visual Studio Code

Lua & C API snippets for [Defold Engine](https://www.defold.com/) is available on [marketplace](https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets).  

All Lua and C/C++ methods, messages,  properties and brief descriptions are included.

[![Github](https://img.shields.io/static/v1?label=Github&message=v1.2.178&color=blue)](https://github.com/selimanac/defold-vsc-snippets)


[![vcs](https://img.shields.io/static/v1?label=Visual%20Studio%20Marketplace&message=v1.2.178&color=blue)](https://marketplace.visualstudio.com/items?itemName=selimanac.defold-vsc-snippets)
------------


![vcs](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/vcs.png)


### Ordered Tabstops

![Ordered Tabstops](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/orderedtabstops.gif)

### Message Generation


#### Examples: 
Type `play_sound` and it will generate  `msg.post(receiver, "play_sound", {[delay], [gain]})`

Type `model_animation_done` and it will generate `msg.post(receiver, "model_animation_done", {animation_id, playback})`

![focus](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/input_focus.gif)

![focus](https://github.com/selimanac/defold-vsc-snippets/raw/master/images/clear_color.gif)






## Recommended Settings & Extension

Add Defold `files.associations` to your `settings.json` file. Also setting `editor.snippetSuggestions` to `bottom` change the order relative to suggestions. 

```json
"files.associations": {
        "*.script": "lua",
        "*.gui_script": "lua",
        "*.render_script": "lua",
        "*.editor_script": "lua"
      },
"editor.snippetSuggestions": "bottom"
```  

##  Recommended Extension

* [EmmyLua](https://marketplace.visualstudio.com/items?itemName=tangzx.emmylua) (Suggested)
* [Lua language support for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=keyring.Lua)
* [Lint Lua scripts with luac or luajit](https://marketplace.visualstudio.com/items?itemName=dcr30.lualinter)
* [Improved Lua syntax highlighting](https://marketplace.visualstudio.com/items?itemName=jep-a.lua-plus)
* [Support go to defintion and List Document Symbols.](https://marketplace.visualstudio.com/items?itemName=xxxg0001.lua-for-vscode)
* [Intellisense and Linting for Lua](https://marketplace.visualstudio.com/items?itemName=trixnz.vscode-lua)


## Json Parser

There is a Python script which download and parse the latest version of the Defold API Reference available on [Github repo](https://github.com/selimanac/defold-vsc-snippets).


