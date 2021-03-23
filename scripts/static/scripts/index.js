$(document).ready(function() {
	async function round_1(){
		await $.ajax({
			url: 'round_1/',
			success: function (data) {
				console.log(data);
			}
		});
	}

	$('#round_1').click(function(){
		return new Promise((res,rej)=>{
			round_1();
		})	
	});

	async function round_2(){
		await $.ajax({
			url: 'round_2/',
			success: function (data) {
				console.log(data);
			}
		});
	}

	$('#round_2').click(function(){
		return new Promise((res,rej)=>{
			round_2();
		})	
	});

});	