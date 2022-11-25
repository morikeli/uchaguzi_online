const MaleRegisteredVoters = document.getElementById("males").value;
const FemaleRegisteredVoters = document.getElementById("females").value;

document.addEventListener("DOMContentLoaded", () => {
new Chart(document.querySelector('#votersChart'), {
	type: 'doughnut',
	data: {
	labels: [
		'Males',
		'Females',
	],
	datasets: [{
		label: 'Registered Voters',
		data: [
			MaleRegisteredVoters, FemaleRegisteredVoters, 
		],
		backgroundColor: [
			'#09ac52',
			'#ec0b0b',
		],
		hoverOffset: 4
	}]
	}
});
});
