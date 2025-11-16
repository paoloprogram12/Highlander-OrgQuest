async function send() {
  let search_element = document.getElementById("search");
  let phrase_list = search_element.value.trim().split(",").filter(s => s.trim() !== "");

  let response = await fetch("http://localhost:8000/scores", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(phrase_list),
  });
  let data = await response.json();

  // Sort data by score descending
  data.sort((a, b) => b.score - a.score);

  // Determine threshold based on number of labels
  let threshold = phrase_list.length === 1 ? 0.375 : 0.35;

  // Filter by threshold
  let filtered = data.filter(item => item.score > threshold);

  // Apply restrictions: min 3, max 8
  let final_results = [];
  if (filtered.length < 3) {
    // Take top 3 clubs regardless of score
    final_results = data.slice(0, 3);
  } else if (filtered.length > 8) {
    // Take top 8 from filtered results
    final_results = filtered.slice(0, 8);
  } else {
    // Use filtered results as-is
    final_results = filtered;
  }

  // Display results as cards
  let results_div = document.getElementById("results");
  results_div.innerHTML = "";

  final_results.forEach((item) => {
    let card = document.createElement("div");
    card.className = "club-card";
    card.textContent = item.name;
    results_div.appendChild(card);
  });
}
