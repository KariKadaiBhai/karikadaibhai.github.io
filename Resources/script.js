const configPath = './Resources/progs/config.json';
let config = {};

// Function to fetch configuration from config.json
async function fetchConfig() {
  const response = await fetch(configPath);
  config = await response.json();
  return config; // Ensure config is returned
}

// Use an async function to ensure config is fetched before proceeding
async function initializeApp() {
  await fetchConfig(); // Wait for config to load

  const pathToFilesJSON = config.pathToFilesJSON;
  const pathToPasswordsJSON = config.pathToPasswordsJSON;
  const cookieExpiryTimeInMinutes = config.cookieExpireTimeInMinutes;

  // Function to create a cookie
  function setCookie(name, value, minutes) {
    const date = new Date();
    date.setTime(date.getTime() + minutes * 60 * 1000); // Set expiration time in milliseconds
    const expires = 'expires=' + date.toUTCString();
    document.cookie = name + '=' + value + ';' + expires + ';path=/';
  }

  // Function to get a cookie value by name
  function getCookie(name) {
    const nameEQ = name + '=';
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');
    for (let i = 0; i < cookieArray.length; i++) {
      let c = cookieArray[i].trim();
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  // Function to prompt for a password and check against passwords.json
  async function promptForPassword() {
    const response = await fetch(pathToPasswordsJSON);
    const passwordsData = await response.json();

    // Check if any existing cookie matches
    for (const user in passwordsData) {
      const passwordData = passwordsData[user];
      if (getCookie(passwordData.cookieData) === 'true') {
        return true; // Skip prompt if cookie is found
      }
    }

    const enteredPassword = prompt('Sollappa Ennaa?');

    // Check if enteredPassword matches any password in passwordsData
    for (const user in passwordsData) {
      const passwordData = passwordsData[user];
      if (enteredPassword === passwordData.password) {
        setCookie(passwordData.cookieData, 'true', cookieExpiryTimeInMinutes);
        return true;
      }
    }

    return false; // Return false if no match is found
  }

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

  // Check for the password before rendering the content
  promptForPassword().then((isAuthenticated) => {
    if (isAuthenticated) {
      document.getElementById('irrungabhai').className = 'visibleH2';
      document.getElementById('drivermairu').className = 'hiddenH2';
      fetch(pathToFilesJSON)
        .then((response) => response.json())
        .then((jsonData) => {
          if (Object.keys(jsonData).length === 0) {
            document.getElementById('no_progs_div').className =
              'no_progs_visible';
          } else {
            document.getElementById('no_progs_div').className =
              'no_progs_hidden';
            for (const programId in jsonData) {
              const programData = jsonData[programId];
              const pane = createPane(programId, programData);
              document.getElementById('container').appendChild(pane);
            }
          }
        })
        .catch((error) => {
          console.error('Error loading JSON file:', error);
        });
    } else {
      document.getElementById('irrungabhai').className = 'hiddenH2';
      document.getElementById('drivermairu').className = 'visibleH2';
      document.getElementById('no_progs_div').className = 'no_progs_visible';
      document.getElementById('no_progs_h1').innerHTML =
        'Day and Night okkandhu ready pandravanuku thaan theriyum.. unaku laam enna _____ ah theriyum... <br> Password thappa potuta.. correct ah podu..';
    }
  });
}

// Call the initialize function to start the application
initializeApp();
