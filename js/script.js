$(function() { // quando o documento estiver pronto/carregado

    function exibir_funcionarios() {
        $.ajax({
            url: 'http://localhost:5000/listar_funcionarios',
            method: 'GET',
            dataType: 'json',
            success: listar_funcionarios,
            error: function() {
                alert("erro ao ler dados, verifique o backend");
            }
        });
        function listar_funcionarios (funcionarios) {
            $('#corpoTabelaFuncionarios').empty();
            mostrar_conteudo("tabelaFuncionarios");
            for (var i in funcionarios) {
                lin = '<tr>' +
                '<td>' + funcionarios[i].nome + '</td>' +
                '<td>' + funcionarios[i].cpf + '</td>' +
                '</tr>';
                $('#corpoTabelaFuncionarios').append(lin);
            }
        }
    }

    function mostrar_conteudo(identificador) {
        $("#tabelaFuncionarios").addClass('invisible');
        $("#conteudoInicial").addClass('invisible');
        $("#"+identificador).removeClass('invisible');
    }

    $(document).on("click", "#linkListarFuncionarios", function() {
        exibir_funcionarios();
    });

    $(document).on("click", "#linkInicio", function() {
        mostrar_conteudo("conteudoInicial");
    });

    $(document).on("click", "#btIncluirFuncionario", function() {
        nome = $("#campoNome").val();
        cpf = $("#campoCPF").val();
        var dados = JSON.stringify({ nome: nome, cpf: cpf});
        $.ajax({
            url: 'http://localhost:5000/incluir_funcionario',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: dados,
            success: funcionarioIncluido,
            error: erroAoIncluir
        });
        function funcionarioIncluido (retorno) {
            if (retorno.resultado == "ok") {
                alert("Funcionario incluído com sucesso!");
                $("#campoNome").val("");
                $("#campoCPF").val("");
            } else {
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoIncluir (retorno) {
            alert("ERRO: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });

    $('#modalIncluirFuncionario').on('hide.bs.modal', function (e) {
        if (! $("#tabelaFuncionarios").hasClass('invisible')) {
            exibir_funcionarios();
        }
    });

    mostrar_conteudo("conteudoInicial");
});