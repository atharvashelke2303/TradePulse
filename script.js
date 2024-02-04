const url = 'https://weather-by-api-ninjas.p.rapidapi.com/v1/weather?city=Mumbai';
const options = {
  method: 'GET',
  headers: {
    'X-RapidAPI-Key': '6de2e5278bmsh45928c7583c6fa8p1fcc8fjsn51cac4044660',
    'X-RapidAPI-Host': 'weather-by-api-ninjas.p.rapidapi.com'
  }
};

(async () => {
  try {
    const response = await fetch(url, options);
    const result = await response.text();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
})();
