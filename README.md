# RUNPLS 
Runpls is a cli-command orchestrator that I made cause I hate the fact that I have to press the up keyword 10x just to run the sequence of commands I need to run multiple times.

Yes, I know I'd rather spend 5 days automating a task I could simply do for 5 seconds but that's the entire point of life. 

** But why not use tools like Make? **
- I don't know how to use Make plus for some wierd reason Make doesn't work as I intend it to be

## Core Features
1. Command Orchestration
    - You can run cli commands much quicker 
2. Make your commands with YAML
    - Actually, this is more of a design choice because who on earth would make another mark up language just for this????

## How it works
The process is simple:
1. Make a runpls.yaml file
2. Insert your commands there
3. type the command ```runpls {Command}```

## Future features
1. Global commands
    - You can make commands that run globally
2. Custom runpls.yaml file names
    - Hopefully you can simply use other file names such as main.yaml,commands.yaml, or my favorite runplsplspls.yaml if you really need to make it work.
3. TOML integration
    - Just saw toml now and it might be based I'm not so sure though.

## How to Contribute
For real though just send me a message to my [Linkedin](https://www.linkedin.com/in/will-vincent-parrone-8763311ba/?originalSubdomain=ph) or send me an [email](mailto:wvparrone@gmail.com).

Feel free to add your own commits here just organize the message with this template:
"feat:<description>" for features
"fix:<description>" for bugfixes
