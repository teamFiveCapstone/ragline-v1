1.) Run

```
npm install @langchain/core@latest @langchain/community @langchain/textsplitters pdf-parse
```

2.) Add "type": "module" to package.json

3.) Create a input and output folder and place your pdf in the input folder

4.) Run

```
node main.js
```

5.) View the output in output folder
//langchain seems to have recursive text splitter, token splitter or text splitter all of which you can change the chunk size and overlap. Doesn't have sentence or paragraph though
