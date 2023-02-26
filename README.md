# Reptyl
Reptyl is a cross-platform command line shell that supports execution of commands in natural language 
![index3](https://user-images.githubusercontent.com/114559605/221433243-8ca74d72-b173-47c2-ba70-6827eb516b1f.png)


## INSTALLATION
You will need Python in order to use Reptyl. With Python installed, run the following command to install Reptyl: `pip install -U reptyl`
## LAUNCH THE SHELL
First of all know that a file called `config.json` must be present in the folder where you will initialize Reptyl. So create a file called config.json with the following content inside; `{"AI_settings": {"enabled":true ,"use_model":"GPT3:text-davinci-003", "apikey":"sk-XXX"},"console_preferences":{}}`
Replace `sk-XXX` with your openai api-key.
To launch Reptyl Shell just import the `reptyl` module with `import reptyl.reptyl` in a Python shell. You will now be able to run natural language commands on your machine. **Warning: the commands executed will not ask for confirmation so they could potentially cause damage to your system if executed incorrectly.**

Some examples of commands to test the Reptyl features are:

`open youtube and play a song from the 80s`

`create a directory called mydir and create 10 more folders inside`

`tell me where I am`

`port forward on port 8080`

`Download a random photo from web and set it as desktop background`

`create a python file in this directory with the code inside to hack the nasa site`

