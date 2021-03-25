$(document).ready(function() {
	async function round_1(){
		await $.ajax({
			url: 'round_1/',
			success: function (data) {
				$('#time_1').text("Esta pregunta tardo " + data["round_1"][1] + " segundos en ser contestada");
				$('#answer_1').text("Aparece " + data["round_1"][0][1] + " veces");
				$('#answer_2').text("Aparece " + data["round_1"][0][1] + " veces");
				$('#answer_3').text("Aparece " + data["round_1"][0][2] + " veces");
			}
		});
	}

	$('#round_1').click(function(){
		$('#time_1').text("");
		$('#answer_1').text("");
		$('#answer_2').text("");
		$('#answer_3').text("");
		return new Promise((res,rej)=>{
			round_1();
		})	
	});

	async function round_2(){
		await $.ajax({
			url: 'round_2/',
			success: function (data) {
				console.log(data)
				$('#time_2').text("Esta pregunta tardo " + data["round_2"][1] + " segundos en ser contestada");
				//$('#answer_4').text(data["round_2"][0]);
				create_episodes_origin_table(data["round_2"][0]);
			}
		});
	}

	$('#round_2').click(function(){
		$('#time_2').text("");
		$('#second_round_table tbody').empty();
		return new Promise((res,rej)=>{
			round_2();
		})	
	});

	function create_episodes_origin_table(data){
		for (const [key, value] of Object.entries(data)) {
			//TODO: CAMBIAR KEY POR NOMBRE
			episode = '<tr><td>'+ key +'</td> <td> Cantidad de origenes distintos: '+ value[0] +'</td></tr>'
			origins = '<tr><td>'+ value[1]+'</td></tr>'
			$('#second_round_table tbody').append(episode)
			$('#second_round_table tbody').append(origins)
		}
	}

});	