$("#cep").focusout(function(){
	$.ajax({
	//O campo URL diz o caminho de onde virá os dados
	url: 'https://viacep.com.br/ws/'+$(this).val()+'/json/unicode/',
    //Define o tipo de dado para JSON
	dataType: 'json',
	//SUCESS função executada caso consiga ler a fonte de dados com sucesso
	success: function(endereco){
	    $("#rua").val(endereco.logradouro);
		$("#bairro").val(endereco.bairro);
		$("#cidade").val(endereco.localidade);
		$("#estado").val(endereco.uf);
		}
	});
});
