# py_pcgamingwiki_parser
Python parser for PCgamingwiki

This is very simple and ham-fisted. I find pcgamingwiki's api convoluted compared to mediawiki's overall structure. 
This takes command-line arguments within quotes to return values on pcgamingwiki. 
These values are on new lines and separated by "==". 

This also has a built in dictionary for each entry in the output, for every key, `pagedata[key] = val` can be accessed. 
 
For now, simply run the release from cmd likethis: 

`pcgamingwiki.exe "elden ring"` 

or Run to receive a popup window asking to "enter game". 

![Screenshot 2022-12-07 155157](https://user-images.githubusercontent.com/98753696/206305402-489cc227-c6fc-4dbd-b9fb-bf2afecb5899.png)

an output file of "output.txt" contains all values. 

Secondarily, you can simple run and a pop up window will request "Enter game"
