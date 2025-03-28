// Função para carregar a lista de animais
function carregarAnimais() {
    fetch('http://127.0.0.1:5000/animais')
        .then(response => response.json())
        .then(animais => {
            const lista = document.getElementById('animais-lista');
            lista.innerHTML = ''; // Limpa a lista antes de adicionar os novos itens

            animais.forEach(animal => {
                const div = document.createElement('div');
                div.innerHTML = `<strong>${animal.nome}</strong> (${animal.especie}, ${animal.raca}, ${animal.idade} anos)`;
                lista.appendChild(div);
            });
        })
        .catch(error => console.error('Erro ao carregar animais:', error));
}

// Função para adicionar um novo animal
document.getElementById('add-animal-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = document.getElementById('nome').value;
    const especie = document.getElementById('especie').value;
    const raca = document.getElementById('raca').value;
    const idade = document.getElementById('idade').value;

    const newAnimal = {
        nome: nome,
        especie: especie,
        raca: raca,
        idade: idade
    };

    fetch('http://127.0.0.1:5000/animais', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newAnimal)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.message); // Exibe a mensagem de sucesso
        carregarAnimais(); // Atualiza a lista de animais
    })
    .catch(error => console.error('Erro ao adicionar animal:', error));
});

// Carregar os animais quando a página for carregada
window.onload = carregarAnimais;
