const unitOptions = {
    l: ["mm", "cm", "m", "km"],
    w: ["mg", "cg", "g", "kg"]
}

function updateUnits() {
    const category = document.getElementById("category").value
    const u1 = document.getElementById("unit1")
    const u2 = document.getElementById("unit2")

    u1.innerHTML = ""
    u2.innerHTML = ""

    unitOptions[category].forEach(unit => {
        u1.options[u1.options.length] = new Option(unit, unit)
        u2.options[u2.options.length] = new Option(unit, unit)
    });
}

async function sendData() {
    const payload = {
        category: document.getElementById("category").value,
        val: document.getElementById("val").value,
        unit1: document.getElementById("unit1").value,
        unit2: document.getElementById("unit2").value,
    }

    const response = await fetch('/convert', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    })

    const data = await response.json()
    document.getElementById("result").innerText = `${data.result}`
}

updateUnits()
