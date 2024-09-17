const themeToggleBtn = document.getElementById('theme-toggle');
const themeStyle = document.getElementById('theme-style');

// Флаг для отслеживания текущей темы
let isDarkTheme = false;

themeToggleBtn.addEventListener('click', () => {
  if (isDarkTheme) {
    // Если тема тёмная, переключаем на светлую
    themeStyle.setAttribute('href', 'static/light-theme.css');
    isDarkTheme = false;
  } else {
    // Если тема светлая, переключаем на тёмную
    themeStyle.setAttribute('href', 'static/dark-theme.css');
    isDarkTheme = true;
  }
});
