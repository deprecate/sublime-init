Sublime Yeoman
===================

A Sublime Text 2 plug-in to allow creating any kind of project from your own custom templates (based on the former [STProjectMaker](https://github.com/bit101/STProjectMaker)). Currently in alpha.

Includes a `.sublime-build` file for running `npm install && bower install` for you once your project has been scaffolded.

![](https://f.cloud.github.com/assets/110953/819687/680e6e5e-efb6-11e2-869a-9ffedfb101e4.jpg)

## Currently includes templates out of the box for

* AngularJS
* Backbone
* Ember
* Chrome App
* RequireJS
* WebApp

Templates are stored in the `/Templates` directory and can contain any arbitrary boilerplate you would like to use. We encourage the inclusion of [Grunt](http://gruntjs.com) (and a Gruntfile) for templates where possible.


## Installation

### Manually:

There are two ways of installing sublime-init:
#### Method 1:
1. Create a folder named `SublimeYeoman` in the `Packages` folder for Sublime Text 2.

   (If you're not sure where your Packages folder is, Go to: menu --> `Preferences/Browse Packages...`)

    -or-

    `{home}/Library/Application Support/Sublime Text 2/Packages/` is the defalt path on a MAC.
    
2. Clone or download this project into the folder `SublimeYeoman` that you have created.

   The clone or download will create a folder named `sublime-init`.
   
3. Once the colne or download has completed proccede to the new folder `sublime-init`.

   (`{home}/Library/Application Support/Sublime Text 2/Packages/SublimeYeoman/sublime-init`)
   
4. Select all the contents in the `sublime-init` folder and move them to the folder that you had created named `SublimeYeoman`.

5. see P.S.

#### Method 2:
1. Clone or download `sublime-init` into your `Packages` folder. (see Method 1 if needing help locating this folder)

2. Once clone or download is complete change the folder named `sublime-init` to `SublimeYeoman`.

3. see P.S.

##### P.S : You need to restart your editor after installing the plugin.

#### To clone from command line:
On MAC:

1.Open Terminal or your application of choice.

2.`$cd` into the `Packages` folder of Sublime Text 2.

The Default path for Sublime Text 2 is `{home}/Library/Application Support/Sublime Text 2/Packages/`

3. run this command:`$git https://github.com/yeoman/sublime-init.git`

4. Follow steps from Method 1 -Step 3 or Method 2 -Step 2.



#### Set up a key binding - (Optional) -
I like to override Control-Shift-N

Go to: menu --> `Preferences/Key Bindings - User`

	[
		{ "keys": ["ctrl+shift+n"], "command": "project_maker" }
	]

## Usage

Invoke "SublimeYeoman" from the command palette to show a Quick Panel list of available templates.
Top Menu --> `Tools` --> `Command Palette` and start typing `SublimeYeoman`. If you used the optional `Key Binding` it will populate next to the Package name.

![screen shot 2013-07-18 at 16 17 17](https://f.cloud.github.com/assets/110953/820070/4c290c7e-efbd-11e2-9a0c-2eb4b4425d75.png)

Choose the template to base your project on:

![screen shot 2013-07-18 at 16 17 26](https://f.cloud.github.com/assets/110953/820069/4c22802a-efbd-11e2-8eca-74712407b96a.png)


You will be prompted to enter a path for your new project. You may be prompted for values for any replaceable tokens in any template files or file names. Enter the values you want to use.

![screen shot 2013-07-18 at 16 17 32](https://f.cloud.github.com/assets/110953/820067/4c1b53fe-efbd-11e2-93d3-2fb66522021c.png)


Newly created project folder will be opened up in Sublime Text:

![screen shot 2013-07-18 at 16 17 41](https://f.cloud.github.com/assets/110953/820068/4c19005e-efbd-11e2-801e-0f2d5e9fd7f6.png)

## Creating and Modifying Templates

A template is simply a folder stored in `<sublime packages dir>/SublimeYeoman/Templates/`. It can contain any number and types of files and nested folders of files.

## Setting up the build system

Sublime populates its Tools/Build System menu based on the “.sublime-build” files stored in the Sublime “Packages” directory. 

Should one need to locate this, it can be found in “~/Library/Application Support/Sublime Text 2/Packages/User” (if using OS X) or the corresponding Packages/User directory on other platforms. Copy and paste the `yeoman.sublime-build` file into Packages directory.

Builds can be executed using a keyboard shortcut (Command+B on Mac is the default on Mac or F7 on Windows), via the Tools menu or when a file is saved. If a project is currently open, the build system we last selected (e.g grunt) will be remembered.

### Tokens

Text files in the template may contain replaceable tokens in the form of `${{token_name}}`. When you create a new project, you will be prompted for values to use for each token found. The same token can be used multiple times in multiple files. You will only be prompted a single time for its value.

Example:

	Hello from ${{user_name}}

when supplied a value of `Paul` for the `user_name` token will become:

	Hello from Paul

### Tokenized File Names

Template file names may also be tokenized using the form `_token_name_.ext`. The leading underscore, token name and trailing underscore will be replaced by the value given.

Example:

	/foo/bar/baz/_info_file_.text

when supplied with a value of `data` for the `info_file` token will become:

	/foo/bar/baz/data.text


### Predefined Tokens

There are two predefined tokens:

`${{project_path}}` in text files will be replaced by the absolute path of the new project directory.

`${{project_name}}` in text files or `_project_name_` as a file name will be replaced by the base name of the project directory.

Example:

Project path is `/foo/bar/baz/MyProject/`

`project_path` will be replaced by `/foo/bar/baz/MyProject/`

`project_name` will be replaced by `MyProject`

### Sublime Project files

If the chosen template has a `.sublime-project` file in the top level, that file will be copied over and processed like any other file in the template. However, if this does not exist, a default `.sublime-project` file will be created using the `project_name` token as its base name. 

## FAQ

### What are the limitations of the current plugin?

Sublime Yeoman currently ships with samples static templates for a number of different types of projects. These templates are the output of the corresponding Yeoman generators, however we eventually intend on shelling out to the `yo` binary to provide access to all Yeoman community generators.

### What about Sublime Text 3 support?

We are currently evaluating the usefulness of this project through an alpha ST2 version being made available. If there is enough interest in an ST3 implementation, we will attempt to work on and support that too. 

### How do you ignore files?

You don't want to try to do token replacement in binary files. The plug-in has a long list of file types that it will ignore when doing token replacement. You can always add your own if any files in your templates cause a problem. The list is contained in the `yeoman.sublime-settings` file. Note, these files _will_ be copied into the project. They will just not be parsed for tokens.


## License

[BSD license](http://opensource.org/licenses/bsd-license.php)
Copyright (c) Google
