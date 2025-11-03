import { PDFLoader } from "@langchain/community/document_loaders/fs/pdf";
import { RecursiveCharacterTextSplitter } from "@langchain/textsplitters";
import fs from "fs";
import path from "path";

const fileNames = ["lion-quick-guide", "ANAC+2024+Digital"];
const fileName = fileNames[0];

async function main() {
  const inputFile = path.resolve(`./input/${fileName}.pdf`);
  const loader = new PDFLoader(inputFile, { splitPages: false });
  const docs = await loader.load();

  const splitter = new RecursiveCharacterTextSplitter({
    chunkSize: 1000,
    chunkOverlap: 200,
  });
  const chunks = await splitter.splitDocuments(docs);

  const outputFile = path.resolve(`./output/${fileName}.txt`);
  const separator = "\n------------------------------\n";
  const allText = chunks.map((chunk) => chunk.pageContent).join(separator);

  fs.writeFileSync(outputFile, allText, "utf8");

  console.log("Chunks are saved in the output folder!");
}

main();
