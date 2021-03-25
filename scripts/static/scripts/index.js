$(document).ready(function() {
	async function round_1(){
		await $.ajax({
			url: 'round_1/',
			success: function (data) {
				$('#time_1').text("Esta pregunta tardo " + data["round_1"][1].toString().slice(0, 5) + " segundos en ser contestada");
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
				$('#time_2').text("Esta pregunta tardo " + data["round_2"][1].toString().slice(0, 5) + " segundos en ser contestada");
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
			str_aux = "[ ";
			value[1].forEach(origin => {
				str_aux += origin + ", ";
			});
			str_origin = str_aux.slice(0, -2) + " ]"
			episode = '<tr><td><code>episode </code>'+ key +'</td> <td> Tiene '+ value[0] +' orígenes distintos</td></tr>'
			origins = '<tr><td colspan="2"><code>origins </code>'+ str_origin +'</td></tr>'
			tr = '<tr><td class="col-md-2"><code>episode </code>'+ key +'</td>'
			tr += '<td class="col-md-2"> Tiene '+ value[0] +' orígenes distintos</td>'
			tr += '<td class="col-md-8"><code>origins </code>'+ str_origin +'</td></tr>'
			$('#second_round_table tbody').append(tr)
			// $('#second_round_table tbody').append(episode)
			// $('#second_round_table tbody').append(origins)
		}
	}

});	