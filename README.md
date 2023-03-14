# Reptyl
Reptyl is a cross-platform command line shell that supports execution of commands in natural language 
![index3](https://user-images.githubusercontent.com/114559605/221433243-8ca74d72-b173-47c2-ba70-6827eb516b1f.png)

**The developers of this software are in no way responsible for any damages caused by the use of this software**

## INTRO

The use of the Reptyl shell is intended for experienced developers, who are already very familiar with the use of a terminal. Reptyl will be really useful for this category of users, but it can still be a lot of fun to use for everyone else too. With this particular shell it is possible to issue commands in natural language. For example, you can create entire root folders with precise logics, you can run executables, create files of any kind, browse the internet, change settings on your pc simply by saying what you want to do in natural language. Don't worry about complicated commands. Reptyl will be able to understand even the most complicated things, you will be surprised by this. by default everything happens without root permissions. if you want to run the commands with root you will have to specify it in the command for example "run myprogram.exe with root privileges". Reptyl works on both Windows and all Unix systems, it will automatically recognize your operating system and commands will be executed based on that operating system.

**JOIN THE OFFICIAL DISCORD SERVER FOR ANY QUESTION OR COMMENT ABOUT REPTYL: https://discord.gg/JjKY9BPZtZ**

## DONATE 

If you found this software useful please consider a donation.
You will help 0ut0flin3 improve this and other software.

Bitcoin:  `17AnP1zuvLV9cQrGQi6H6qMLeWeujHzAYX`

Monero: `82qjYLZj6XeTGjeUNm9AQVB78hVGStZd8YU1UKuvWz8QKAzFWZpBpEQFho3jrvUCNQPSqC9nYeEN3b7FQ5REPffNSA2WSDH`

Solana: `6RX2ADdcNWZfaUfuGeHg86AYAoMuLF45Lbgfu3oNGh9i`

Litecoin: `ltc1q4ft4ltjnyt8auqq4m5u7raatftu6mt5snst493`

Ethereum: `0xF3A0246690947669A0bf68147Ba82AC8de576a56`

Polygon / MYST : `0x45320b5B2a8f6073f4a92FFDF149861aBade4B4b`

Thank you

## HOW TO USE
**important: don't use configuration files from older version of Reptyl but always use a new configuration file generated from the version you're actually using**

**If you are on Windows, in way to use the Reptyl shell using Powershell, you have to set the execution policy to "unrestricted" before, by open a new Powershell with Administrator privilieges and typing: `Set-ExecutionPolicy Unrestricted`**

To launch a Reptyl shell you can use Python or use one of the standalone binaries available <a href="http://reptyl.org/download">here</a> .
If you want to use Python install Reptyl module with `pip install -U reptyl` then import the `reptyl` module with `import reptyl.reptyl` in a Python shell. You will be prompted to enter your OpenAI api key on first launch. A new configuration file  will be created if it doesn't exists in the current working directory. In the configuration you can set the `temperature` used for executing commands (defaut is `0`), and you can choose if be asked for confirmation before running the command, accompanied by a description of what the command will do . You can do this by setting `askconfirm` to `true` or `false`. (default is `true`)
From Reptyl version 0.0.0.7, by default, the commands will be generated and executed directly in Bash (if you are on a Unix OS) or in Powershell (if you are on Windows) instead of Python, but for some people can still be useful to generate and execute commands in Python language for many reasons. You can enable Python language for executing commands in the Reptyl shell by setting `use_python` to `true` in the configuration. (default is `false`) If `use_python` is set to `false` Reptyl will use Bash or Powershell depending on the OS you are using.

You will now be able to run natural language commands on your machine. 
**do not execute commands if you do not understand what they do exactly, this could damage your computer**

**Don't ask questions but give orders instead**

Some examples of commands to test the Reptyl features are:


`Create a directory called mydir and create 10 more folders inside`

`Shutdown computer if internet goes off`

`Take a screenshot and save it on the Desktop`

`Set a dark theme`

`Show the incoming requests to my network in the last 24 hours`

`Create a python file in this directory with the code inside to hack the NASA site`

