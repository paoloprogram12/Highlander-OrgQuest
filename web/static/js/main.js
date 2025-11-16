async function send() {
  let search_element = document.getElementById("search");
  let phrase_list = search_element.split(",");
  let response = await fetch("http://localhost:8000/score", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: phrase_list,
  });
  window.innerHTML = await response.data;
}
