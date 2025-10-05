const BASE_URL = "https://cowsay-api-service-70338534109.us-central1.run.app";

// função para exibir resultado no pre
function displayResult(outputElement, result) {
    if (result.error) {
        outputElement.textContent = `ERRO: ${result.message}`;
    } else if (result.art) {
        // Exibe a arte cowsay
        outputElement.textContent = result.art;
    } else {
        // Exibe o histórico formatado como JSON indentado
        outputElement.textContent = JSON.stringify(result, null, 2);
    }
}

// GET usando fetch
async function handleGet(e) {
    e.preventDefault();

    const msg = document.getElementById('msg-get').value;
    const char = document.getElementById('char-get').value;
    const output = document.getElementById('output-get');

    // Constrói a URL com querystring
    const url = `${BASE_URL}/cowsay?msg=${encodeURIComponent(msg)}&char=${encodeURIComponent(char)}`;

    output.textContent = "Carregando...";

    try {
        const response = await fetch(url);

        // Verifica se a resposta HTTP é OK
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.description || `Erro HTTP: ${response.status}`);
        }

        const result = await response.json();
        displayResult(output, result);

    } catch (error) {
        displayResult(output, { error: true, message: error.message });
    }
}

// POST usando fetch
async function handlePost(e) {
    e.preventDefault();

    const msg = document.getElementById('msg-post').value;
    const char = document.getElementById('char-post').value;
    const output = document.getElementById('output-post');

    const data = { msg, char };

    output.textContent = "Carregando...";

    try {
        const response = await fetch(`${BASE_URL}/cowsay`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.description || `Erro HTTP: ${response.status}`);
        }

        const result = await response.json();
        displayResult(output, result);

    } catch (error) {
        displayResult(output, { error: true, message: error.message });
    }
}

// Função para Histórico
async function handleHistory() {
    const output = document.getElementById('output-history');
    output.textContent = "Buscando histórico...";

    try {
        const response = await fetch(`${BASE_URL}/history`);

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.description || `Erro HTTP: ${response.status}`);
        }

        const result = await response.json();
        displayResult(output, result);

    } catch (error) {
        displayResult(output, { error: true, message: error.message });
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // // TODO: adicionar listener no formulário GET
    const formGet = document.getElementById('form-get');
    formGet.addEventListener('submit', handleGet);

    // // TODO: adicionar listener no formulário POST
    const formPost = document.getElementById('form-post');
    formPost.addEventListener('submit', handlePost);

    // // TODO: adicionar listener no botão de histórico
    const btnHistory = document.getElementById('btn-history');
    btnHistory.addEventListener('click', handleHistory);
});