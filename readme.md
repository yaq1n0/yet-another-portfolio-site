Welcome to the source code of yaqinhasan.com

This version of the code is all written from scratch while trying to use as much plain html and css as possible while retaining a responsive UI. 

The website is designed to be as functional as possible while still being pleasing to the eye, without unnecessary web_bloat™ stuff such as unneccessary animations, resource hog JS frameworks and ridiculously long non-human readable files. 

The code was written with clean code principles in mind, keeping in mind modularity, maintainability, scalability and most importantly SIMPLICITY! However, the code in this state was written in about 2 days as of writing this README.md, so it can definitely use some refactoring and cleanup. 

Some things that can be done to make the code better: 
 - Improve consistency in implementation of features 
 - Remove unnecessary CSS repetition where possible, increase the usage of generics, without creating too much unnecessary polymorphism (balance :D )
 - Store the JetBrains Mono font on the webserver/site root, this might be hard because of the variable font, but theoretically possible, and will remove external dependencies

Some features I would like to implement: 
 - Expand theming
    - More base colors
    - More color variations, more complete variations (no skipped permutations)
 - improve top navigation bar with a simple menu drop down for mobile (though I might not do this if it takes some bloated JS module to do so)

The rest of this file is just notes for where I can get the resources used in the site. 
The .svg Icons of other companies are from https://icons.getbootstrap.com, this is mainly used in contact.html

The favicon was made with a favicon generator using an svg generated from https://danmarshall.github.io/google-font-to-svg-path/

The font used globally is JetBrains Mono, obtainable from https://www.jetbrains.com/lp/mono/ or through google's font API https://fonts.google.com/specimen/JetBrains+Mono