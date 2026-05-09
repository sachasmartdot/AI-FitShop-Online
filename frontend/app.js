let selectedProduct = null;

// Load products
fetch("http://127.0.0.1:8000/products")
.then(res => res.json())
.then(data => {
    const container = document.getElementById("products");

    data.forEach(p => {
        const div = document.createElement("div");

        div.innerHTML = `
            <h3>${p.name}</h3>
            <p>${p.price} $</p>
            <button>Select</button>
        `;

        div.querySelector("button").onclick = () => {
            selectedProduct = p;
            alert("Selected: " + p.name);
        };

        container.appendChild(div);
    });
});

// Recommendation
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

// Chat
function sendMsg() {
    const msg = document.getElementById("msg").value;

    fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({message: msg})
    })
    .then(res => res.json())
    .then(data => {
        const chat = document.getElementById("chat");

        chat.innerHTML += "<p><b>You:</b> " + msg + "</p>";
        chat.innerHTML += "<p><b>Agent:</b> " + data.reply + "</p>";
    });
}
