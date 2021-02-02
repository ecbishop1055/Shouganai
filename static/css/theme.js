/*Defines which theme should load next
const themeMap = {
    dark: "light",
    light: "solar",
    solar: "dark"
};

//Loads the existing theme in local storage
const theme =  localStorage.getItem('theme')
    || (tmp = Object.keys(themeMap)[0],
        localStorage.setItem('theme', tmp),
        tmp);
const bodyClass  = document.body.classList;
bodyClass.add(theme);

//Changes the theme via button click    
function toggleTheme() {
    const current = localStorage.getItem('theme');
    const next = themeMap[current];

    bodyClass.replace(current, next);
    localStorage.setItem('theme', next);
}

document.getElementById('themeButton').onclick = toggleTheme;

*/