// Function to create the "pane" div elements
function createPane(programId, programData) {
  const paneDiv = document.createElement('div');
  paneDiv.id = 'pane';
  paneDiv.className = `os-${programId}`;

  const questionDiv = document.createElement('div');
  questionDiv.className = 'question';

  const h1Tag = document.createElement('h1');
  h1Tag.className = 'qnH';
  h1Tag.textContent = programData.ContentToDisplay;

  questionDiv.appendChild(h1Tag);

  const dwnldBtnDiv = document.createElement('div');
  dwnldBtnDiv.className = 'dwnld_btn';

  const aTagOpen = document.createElement('a');
  aTagOpen.href = './Resources/progs/files/' + programData.ReadFile;
  aTagOpen.id = 'atag';
  aTagOpen.className = 'open_a';

  const btnOpen = document.createElement('button');
  btnOpen.id = 'btn';
  btnOpen.className = 'open_btn';
  btnOpen.textContent = 'Open';

  aTagOpen.appendChild(btnOpen);
  dwnldBtnDiv.appendChild(aTagOpen);

  if (programData.Downloadable) {
    const aTagDwnld = document.createElement('a');
    aTagDwnld.href = './Resources/progs/files/' + programData.DownloadFile;
    aTagDwnld.id = 'atag';
    aTagDwnld.className = 'download_a';
    aTagDwnld.setAttribute('download', '');

    const btnDwnld = document.createElement('button');
    btnDwnld.id = 'btn';
    btnDwnld.className = 'download_btn';

    const imgDwnld = document.createElement('img');
    imgDwnld.id = 'download_icon_img';
    imgDwnld.className = 'download_icon_img';
    imgDwnld.src = './Resources/download_icon.png';

    btnDwnld.appendChild(imgDwnld);
    aTagDwnld.appendChild(btnDwnld);
    dwnldBtnDiv.appendChild(aTagDwnld);
  }

  paneDiv.appendChild(questionDiv);
  paneDiv.appendChild(dwnldBtnDiv);

  return paneDiv;
}

// Fetch the JSON data from the file
fetch('./Resources/progs/index.json')
  .then((response) => response.json())
  .then((jsonData) => {
    // Loop through the JSON data and create "pane" div elements
    if (Object.keys(jsonData).length === 0) {
      document.getElementById('no_progs_div').className = 'no_progs_visible';
    } else {
      document.getElementById('no_progs_div').className = 'no_progs_hidden';
      for (const programId in jsonData) {
        const programData = jsonData[programId];
        const pane = createPane(programId, programData);
        document.getElementById('container').appendChild(pane); // Append to the container div
      }
    }
  })
  .catch((error) => {
    console.error('Error loading JSON file:', error);
  });
