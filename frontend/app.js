let selectedProduct = null;

fetch("http://127.0.0.1:8000/products")
.then(res => res.json())
.then(data => {
    const container = document.getElementById("products");

    data.forEach(p => {
        const div = document.createElement("div");
        div.innerHTML = `
            <h3>${p.name}</h3>
            <p>${p.price} $</p>
            <button onclick='selectProduct(${JSON.stringify(p)})'>Select</button>
        `;
        container.appendChild(div);
    });
});

function selectProduct(p) {
    selectedProduct = p;
    alert("Selected: " + p.name);
}

function getRecommendation() {
    const foot = document.getElementById("foot").value;

    fetch("http://127.0.0.1:8000/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            foot_length: parseFloat(foot),
            product: selectedProduct
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Recommended size: " + data.recommended_size +
            " | Confidence: " + data.confidence + "%";
    });
}
