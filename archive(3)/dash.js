document.addEventListener('DOMContentLoaded', function () {
    // Extrair os dados dos datasets
    const mengoData = {
        year: [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
        position: [8, 17, 15, 11, 3, 5, 1, 14, 4, 11, 16, 10, 12, 3, 6, 2, 1],
        points: [66, 54, 55, 52, 61, 64, 67, 44, 61, 50, 45, 52, 49, 71, 56, 72, 90],
        games: [46, 46, 42, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38],
        victories: [18, 13, 14, 15, 17, 18, 19, 9, 15, 12, 12, 14, 15, 20, 15, 21, 28],
        draws: [12, 15, 13, 7, 10, 10, 10, 17, 16, 14, 13, 10, 4, 11, 11, 9, 6],
        losses: [16, 18, 15, 16, 11, 10, 9, 12, 7, 12, 13, 14, 19, 7, 12, 8, 4],
        goals_scored: [66, 51, 56, 44, 55, 67, 58, 41, 59, 39, 43, 46, 45, 52, 49, 59, 86],
        goals_against: [73, 53, 60, 48, 49, 48, 44, 44, 47, 46, 46, 47, 53, 35, 38, 29, 33],
        goals_difference: [-7, -2, -4, 4, 6, 19, 14, -3, 12, -7, -3, -1, -8, 17, 11, 30, 53],
        perc_points_won: [47, 39, 44, 46, 54, 56, 59, 39, 53, 44, 43, 45, 43, 62, 49, 63, 81]
    };

    const tricolorData = {
        year: [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
        position: [3, 3, 11, 1, 1, 1, 3, 9, 6, 4, 9, 2, 4, 10, 13, 5, 6],
        points: [78, 82, 58, 78, 77, 75, 65, 55, 59, 66, 50, 70, 62, 52, 50, 63, 63],
        games: [46, 46, 42, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38],
        victories: [22, 24, 16, 22, 23, 21, 18, 15, 16, 20, 14, 20, 18, 14, 13, 16, 17],
        draws: [12, 10, 10, 12, 8, 12, 11, 10, 11, 6, 8, 10, 8, 10, 11, 15, 12],
        losses: [12, 12, 16, 4, 7, 5, 9, 13, 11, 12, 16, 8, 12, 14, 14, 7, 9],
        goals_scored: [81, 78, 77, 66, 55, 66, 57, 54, 57, 59, 39, 59, 53, 44, 48, 46, 39],
        goals_against: [67, 43, 67, 32, 19, 36, 42, 54, 46, 37, 40, 40, 47, 36, 49, 34, 30],
        goals_difference: [14, 35, 10, 34, 36, 30, 15, 0, 11, 22, -1, 19, 6, 8, -1, 12, 9],
        perc_points_won: [56, 59, 46, 68, 68, 66, 57, 48, 52, 58, 44, 61, 54, 46, 44, 55, 55]
    };

    const labels = mengoData.year;

    // Criar os gráficos
    createChart('points-chart', 'Pontos', labels, mengoData.points, tricolorData.points);
    createChart('position-chart', 'Posição', labels, mengoData.position, tricolorData.position);
    createChart('games-chart', 'Jogos', labels, mengoData.games, tricolorData.games);
    createChart('victories-chart', 'Vitórias', labels, mengoData.victories, tricolorData.victories);
    createChart('draws-chart', 'Empates', labels, mengoData.draws, tricolorData.draws);
    createChart('losses-chart', 'Derrotas', labels, mengoData.losses, tricolorData.losses);
    createChart('goals-scored-chart', 'Gols Marcados', labels, mengoData.goals_scored, tricolorData.goals_scored);
    createChart('goals-against-chart', 'Gols Sofridos', labels, mengoData.goals_against, tricolorData.goals_against);
    createChart('goals-difference-chart', 'Saldo de Gols', labels, mengoData.goals_difference, tricolorData.goals_difference);
    createChart('perc-points-won-chart', '% de Pontos Ganhas', labels, mengoData.perc_points_won, tricolorData.perc_points_won);

});

function createChart(id, label, labels, mengoData, tricolorData) {
    const ctx = document.getElementById(id).getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Flamengo',
                data: mengoData,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1
            }, {
                label: 'São Paulo',
                data: tricolorData,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
