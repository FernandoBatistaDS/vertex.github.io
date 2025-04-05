import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE HTML>
<!--
	Dimension by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Implantação PBI Comercial - Vertex</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/cards.css" />
		<link rel="stylesheet" href="assets/css/list.css" />
		<link rel="stylesheet" href="assets/css/main.css" />
		<noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	</head>
	<body class="is-preload">

		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<div class="logo">
							<img class="logo-vertical-branco" src="assets/logos/logo-vertex-vertical-branco.svg" alt="Logo vertex vertical branco">
							<!-- <span class="icon fa-gem"></span> -->
						</div>
						<div class="content">
							<div class="inner">
								<h1>Implantação PBI Comercial - Vertex</h1>
							</div>
						</div>
						<nav>
							<ul>
								<li><a href="#intro">Intro</a></li>
								<li><a href="#work">Prefácio</a></li>
								<li><a href="#about">Time</a></li>
								<li><a href="#contact">Insights</a></li>
								<li><a href="#elements">Guia</a></li>
							</ul>
						</nav>
					</header>

				<!-- Main -->
					<div id="main">

						<!-- Intro -->
							<article id="intro">
								<h2 class="major">Intro</h2>
								<span class="image main"><img src="assets/logos/logo-vertex-horizontal-limao-neon.png" alt="" /></span>
								<p>Na Vertex Tennis, dados se tornam decisões estratégicas que impulsionam o desempenho e a inovação. Isso não é novidade. Com o objetivo de darmos mais um passo e melhorar ainda mais essa realidade, estamos implementando o Power BI como uma nova ferramenta no fluxo.</p>
								<h4 class="major">Estrutura do Site</h4>
								<p>Nesse site você encontrará as principáis informações sobre uso, insights, manutenção e governança, organizado nos seguintes módulos.</p>


								<ul>
									<li class="card" style="--color:#ececec; --bg-color: #173b2f">
									  <div class="title">Introdução</div>
									  <div class="content">Uma breve descrição do objetivo da implantação com um vídeo explicativo.</div>
									</li>
									<li class="card" style="--color:#ececec; --bg-color:#1d6049">
									  <div class="title">Dashboard</div>
									  <div class="content">Exibe informações principais e métricas relevantes. Além de apresentar uma lista de insghts logo abaixo.</div>
									</li>
									<li class="card" style="--color:#ececec; --bg-color:#169b6e">
									  <div class="title">Guia de Implementação</div>
									  <div class="content">Toda a explicação relacionada as licenças necessárias, suporte e manutenção da ferramenta.</div>
									</li>
								  </ul>

							</article>

						<!-- Work -->
							<article id="work">
								<h2 class="major">Apresentação</h2>
								<p>Veja aqui como é o funcionamento do relatório em Power Bi e como ele irá sanar algumas das suas principáis dores do cotidiano. Além disso, conheça a equipe da Insight Hunters, que estará atuando em parceria com a Vertex nessa etapa de implementação:</p>
								<iframe width="560" height="315" src="https://www.youtube.com/embed/L1mK-tafwjw?si=fddIBoUepdWtWA2i" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
							</article>

						<!-- About -->
							<article id="about">
								<h2 class="major">Insight Hunters <br> Conheça nosso time:</h2>

								<div class="container">
									<div class="card">
									  <img src="https://lh3.googleusercontent.com/a/AGNmyxZ6qSVDtB856uLoGdIQJoPKY712zFFxXm9oj-xZ1g=s96-c" alt="Person" class="card__image">
									  <p class="card__name">Gabriel<br>Penha</p>
									  <span>Telefone: </span>
									  <p class="phone">(71) 99210-9164</p>
									  <button class="btn draw-border"><a href="https://www.linkedin.com/in/gabriel4210"><i class="fa-brands fa-linkedin-in"></i></a></button>
								  
									</div>
									<div class="card">
									  <img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/carol.jpeg?raw=true" alt="Person" class="card__image">
									  <p class="card__name">Carolina<br>Diniz</p>
									  <span>Telefone: </span>
									  <p class="phone">(31) 99238-0507</p>
									  <button class="btn draw-border"><a href="https://www.linkedin.com/in/carolina-diniz-2b80701a4"><i class="fa-brands fa-linkedin-in"></i></a></button>
									</div>
									<div class="card">
									  <img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/fernando.jpeg?raw=true" alt="Person" class="card__image">
									  <p class="card__name">Fernando<br>Batista</p>
									  <span>Telefone: </span>
									  <p class="phone">(11) 98410-1047</p>
									  <button class="btn draw-border"><a href="https://www.linkedin.com/in/fernandobatistads"><i class="fa-brands fa-linkedin-in"></i></a></button>
									</div>
									<div class="card">
										<img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/antonio.jpeg?raw=true" alt="Person" class="card__image">
										<p class="card__name">Antônio<br>Brandenberger</p>
									  <span>Telefone: </span>
										<p class="phone">(21) 99252-2552</p>
										<button class="btn draw-border"><a href="https://www.linkedin.com/in/antonio-brandenberger"><i class="fa-brands fa-linkedin-in"></i></a></button>
									</div>
									<div class="card">
										<img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/matheus.jpeg?raw=true" alt="Person" class="card__image">
										<p class="card__name">Matheus<br>Marques</p>
									  <span>Telefone: </span>
										<p class="phone">(31) 99172-3497</p>
										<button class="btn draw-border"><a href="https://www.linkedin.com/in/matheus-marques-rodrigues"><i class="fa-brands fa-linkedin-in"></i></a></button>
									</div>
									<div class="card">
										<img src="https://github.com/Gabriel4210/Vertex_App/blob/main/Photos/felipe.jpeg?raw=true" alt="Person" class="card__image">
										<p class="card__name">Felipe<br>Acauã</p>
									  <span>Telefone: </span>
										<p class="phone">(14) 99603-9135</p>
										<button class="btn draw-border"><a href="https://www.linkedin.com/in/felipe-acau%C3%A3-88101021b"><i class="fa-brands fa-linkedin-in"></i></a></button>
									</div>
									<div class="card">
										<img src="https://media.licdn.com/dms/image/v2/D4D03AQFrJJGgZBPrQg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1708985390534?e=1749081600&v=beta&t=XfwgWyu_AGypXeYIC8WZb6zqotvDnz9vxMXCd2GfAiQ" alt="Person" class="card__image">
										<p class="card__name">Wendell<br>Pedra</p>
									  <span>Telefone: </span>
										<p class="phone">(11) 99421-5743</p>
										<button class="btn draw-border"><a href="https://www.linkedin.com/in/wendellgpedra/"><i class="fa-brands fa-linkedin-in"></i></a></button>
									</div>
								</div>
								  

							</article>

						<!-- Contact -->
							<article id="contact">
								<h2 class="major">Relatório Power BI</h2>
								<iframe width="900" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiOGIzOGI0ZjEtMDM2Mi00OWIyLTkxNDgtOWE5YmMyYzM0NGNlIiwidCI6ImRmNzFmNmJiLWUzY2MtNGY1Yi1iNTMyLTc5ZGUyNjFiNTFhMiJ9" frameborder="0" allowfullscreen="">
								</iframe>
								<br>
								<br>
								<h4 class="major">Insights Extraídos</h4>
								<p>Abaixo estão algumas das análises destacadas pelo time da Insight Hunters:</p>

								<ul>
									<li class="card" style="--color:#ececec; --bg-color: #173b2f">
									  <div class="title">Desempenho por Categoria de Equipamento</div>
									  <div class="content">Uma breve descrição do objetivo da implantação com um vídeo explicativo.</div>
									</li>
									<li class="card" style="--color:#ececec; --bg-color: #173b2f">
									  <div class="title">Perfil dos Consumidores</div>
									  <div class="content">Exibe informações principais e métricas relevantes. Além de apresentar uma lista de insghts logo abaixo.</div>
									</li>
									<li class="card" style="--color:#ececec; --bg-color: #173b2f">
									  <div class="title">Sazonalidade de Vendas</div>
									  <div class="content">Toda a explicação relacionada as licenças necessárias, suporte e manutenção da ferramenta.</div>
									</li>
									<li class="card" style="--color:#ececec; --bg-color: #173b2f">
									  <div class="title">Distribuição Geográfica</div>
									  <div class="content">Toda a explicação relacionada as licenças necessárias, suporte e manutenção da ferramenta.</div>
									</li>
								</ul>


							</article>

						<!-- Elements -->
						<article id="elements">
							<h2 class="major">Guia de Implementação</h2>

							<section>
								<h2>1. Introdução</h2>
								<p>Este guia apresenta diretrizes para a adoção eficaz do Power BI na Vertex, assegurando seu uso eficiente e garantindo governança sólida. O objetivo é proporcionar valor aos usuários, prevenindo a subutilização da ferramenta ao longo do tempo.</p>
								<h2>2. Objetivos</h2>
								<ul>
									<li>Impulsionar a adoção do Power BI.</li>
									<li>Garantir governança e segurança dos dados.</li>
									<li>Definir papéis e responsabilidades de cada usuário.</li>
									<li>Criar um plano de atualização e manutenção da solução.</li>
								</ul>
								<h2>3. Licenças e Acessos</h2>
								<p>A quantidade e tipos de licenças deverão ser analisadas pela Vertex e disponibilizadas de acordo com a quantidade de licenças adquiridas.</p>
								<p>O Power BI Free não deve ser utilizado para compartilhamento de conteúdo com outros usuários, pois os dados são expostos publicamente, o que pode comprometer informações sensíveis da empresa. Isso inclui dados pessoais de vendedores, protegidos pela Lei Geral de Proteção de Dados Pessoais (LGPD), além de informações estratégicas sobre fornecedores, que poderiam ficar acessíveis à concorrência.</p>
								<p>O Power BI Pro é adequado à Vertex. As vantagens desse plano são o compartilhamento seguro, a possibilidade de criar workspaces para colaboração em equipe, 8 atualizações diárias dos dados e capacidade de armazenamento de 10 GB por usuário. O valor atualmente é de 10 dólares por usuário/mês. Tanto o desenvolvedor dos dashboards quanto os usuários devem ter a conta Pro para esse compartilhamento.</p>
								<p>O Power BI Premium não é necessário no presente momento da empresa, sendo recomendada uma avaliação de migração baseada em volume de dados e número de usuários futuramente.</p>

								<h2>4. Papéis e Responsabilidades</h2>
								<h3>4.1 TI (Suporte e Governança)</h3>
								<ul>
									<li>Concede acessos e gerencia segurança.</li>
									<li>Monitora uso e desempenho.</li>
									<li>Suporta usuários e resolve dúvidas técnicas.</li>
								</ul>
								<h3>4.2 Analistas</h3>
								<ul>
									<li>Criam relatórios e dashboards.</li>
									<li>Garantem qualidade e confiabilidade dos dados.</li>
									<li>Utilizam bases externas documentadas e aprovadas pela TI.</li>
								</ul>
								<h3>4.3 Gerentes e Diretores</h3>
								<ul>
									<li>Acompanham KPIs e tomam decisões estratégicas.</li>
									<li>Podem solicitar novos relatórios via fluxo formal, por e-mail e com cópia para o grupo de gerentes e diretores com informações mínimas, como:</li>
									<ul>
										<li>Nome do Relatório Afetado</li>
										<li>Justificativa para mudança</li>
										<li>Tipos de alteração (ajuste visual, inclusão de novos dados, melhoria de desempenho)</li>
									</ul>
								</ul>
								<h3>4.4 Supervisores e Vendedores</h3>
								<ul>
									<li>Usam dashboards para acompanhar metas.</li>
									<li>Reportam problemas nos dados.</li>
									<li>Podem solicitar novos relatórios ou alterações via fluxo formal, por e-mail, conforme descrito no item 3.3 acima.</li>
								</ul>
								<h2>5. Segurança e Controle de Acesso</h2>
								<ul>
									<li>Os dados da empresa não devem ser compartilhados com pessoas não autorizadas.</li>
									<li>Não é permitido fazer cópia dos dashboards para uso pessoal.</li>
									<li>Acesso restrito por região (baseado na tabela Employees).</li>
									<li>Monitoramento de logs no Power BI Service.</li>
									<li>Implementação de Data Loss Prevention (DLP) para restringir exportação de dados sensíveis.</li>
									<li>Plano de resposta a incidentes em caso de vazamento ou acesso indevido.</li>
								</ul>
								<h2>6. Compartilhamento de Relatórios</h2>
								<ul>
									<li>Os relatórios serão compartilhados via Power BI Service.</li>
									<li>Haverá controle de permissões detalhado para evitar exportação indevida.</li>
									<li>Política clara sobre o uso de impressões em apresentações internas.</li>
								</ul>
								<h2>7. Plano de Atualização e Manutenção</h2>
								<h3>7.1 Curto prazo (1 mês)</h3>
								<ul>
									<li>Treinamento básico para usuários.</li>
									<li>Ajustes na segurança de acessos.</li>
									<li>Criação dos primeiros dashboards estratégicos.</li>
								</ul>
								<h3>7.2 Médio prazo (2 a 3 meses)</h3>
								<ul>
									<li>Análise das métricas de adoção.</li>
									<li>Documentação oficial dos relatórios.</li>
									<li>Automação de importação de bases externas.</li>
								</ul>
								<h3>7.3 Longo prazo (4+ meses)</h3>
								<ul>
									<li>Avaliação da necessidade de migração para Power BI Premium.</li>
									<li>Evolução contínua dos dashboards conforme feedback e solicitações formalizadas.</li>
								</ul>
								<h2>8. Métricas de Sucesso</h2>
								<ul>
									<li>Taxa de Adoção: Monitoramento de usuários ativos semanalmente.</li>
									<li>Uso dos Relatórios: Frequência de acesso e identificação de dashboards subutilizados.</li>
									<li>Tempo Médio de Resolução de Dúvidas: Avaliação da eficiência do suporte.</li>
									<li>Painel de Governança no Power BI para acompanhamento das métricas.</li>
								</ul>
								<h2>9. Estratégia para Garantir a Adoção</h2>
								<ul>
									<li>Criação de um Grupo de Super Usuários, capacitados para apoiar suas equipes.</li>
									<li>Calendário de reuniões periódicas para revisão do uso do Power BI e para propor ações caso o uso esteja abaixo do adequado.</li>
									<li>Dashboard mobile-friendly para acesso facilitado.</li>
									<li>Gamificação: Reconhecimento para os usuários mais engajados.</li>
									<li>Comunicação interna: E-mails e eventos para reforçar o uso.</li>
								</ul>
								<h2>10. Conclusão e Próximos Passos</h2>
								<p>O guia deve ser seguido por todos os usuários para garantir o sucesso da implementação. Dúvidas podem ser encaminhadas à equipe de TI ou aos Analistas de Vendas.</p>
								<p>A primeira análise de adoção será realizada após 3 meses, permitindo ajustes conforme necessário.</p>
								<hr />
							</section>
							<section>
								<ul class="actions">
									<li><a href="#" class="button">Baixar Guia Completo em PDF</a></li>
								</ul>
							</section>
						</article>
						<!-- <article id="elements">
								<h2 class="major">Elements</h2>

								<section>
									<h3 class="major">Text</h3>
									<p>This is <b>bold</b> and this is <strong>strong</strong>. This is <i>italic</i> and this is <em>emphasized</em>.
									This is <sup>superscript</sup> text and this is <sub>subscript</sub> text.
									This is <u>underlined</u> and this is code: <code>for (;;) { ... }</code>. Finally, <a href="#">this is a link</a>.</p>
									<hr />
									<h2>Heading Level 2</h2>
									<h3>Heading Level 3</h3>
									<h4>Heading Level 4</h4>
									<h5>Heading Level 5</h5>
									<h6>Heading Level 6</h6>
									<hr />
									<h4>Blockquote</h4>
									<blockquote>Fringilla nisl. Donec accumsan interdum nisi, quis tincidunt felis sagittis eget tempus euismod. Vestibulum ante ipsum primis in faucibus vestibulum. Blandit adipiscing eu felis iaculis volutpat ac adipiscing accumsan faucibus. Vestibulum ante ipsum primis in faucibus lorem ipsum dolor sit amet nullam adipiscing eu felis.</blockquote>
									<h4>Preformatted</h4>
									<pre><code>i = 0;

while (!deck.isInOrder()) {
    print 'Iteration ' + i;
    deck.shuffle();
    i++;
}

print 'It took ' + i + ' iterations to sort the deck.';</code></pre>
								</section>

								<section>
									<h3 class="major">Lists</h3>

									<h4>Unordered</h4>
									<ul>
										<li>Dolor pulvinar etiam.</li>
										<li>Sagittis adipiscing.</li>
										<li>Felis enim feugiat.</li>
									</ul>

									<h4>Alternate</h4>
									<ul class="alt">
										<li>Dolor pulvinar etiam.</li>
										<li>Sagittis adipiscing.</li>
										<li>Felis enim feugiat.</li>
									</ul>

									<h4>Ordered</h4>
									<ol>
										<li>Dolor pulvinar etiam.</li>
										<li>Etiam vel felis viverra.</li>
										<li>Felis enim feugiat.</li>
										<li>Dolor pulvinar etiam.</li>
										<li>Etiam vel felis lorem.</li>
										<li>Felis enim et feugiat.</li>
									</ol>
									<h4>Icons</h4>
									<ul class="icons">
										<li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
										<li><a href="#" class="icon brands fa-facebook-f"><span class="label">Facebook</span></a></li>
										<li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
										<li><a href="#" class="icon brands fa-github"><span class="label">Github</span></a></li>
									</ul>

									<h4>Actions</h4>
									<ul class="actions">
										<li><a href="#" class="button primary">Default</a></li>
										<li><a href="#" class="button">Default</a></li>
									</ul>
									<ul class="actions stacked">
										<li><a href="#" class="button primary">Default</a></li>
										<li><a href="#" class="button">Default</a></li>
									</ul>
								</section>

								<section>
									<h3 class="major">Table</h3>
									<h4>Default</h4>
									<div class="table-wrapper">
										<table>
											<thead>
												<tr>
													<th>Name</th>
													<th>Description</th>
													<th>Price</th>
												</tr>
											</thead>
											<tbody>
												<tr>
													<td>Item One</td>
													<td>Ante turpis integer aliquet porttitor.</td>
													<td>29.99</td>
												</tr>
												<tr>
													<td>Item Two</td>
													<td>Vis ac commodo adipiscing arcu aliquet.</td>
													<td>19.99</td>
												</tr>
												<tr>
													<td>Item Three</td>
													<td> Morbi faucibus arcu accumsan lorem.</td>
													<td>29.99</td>
												</tr>
												<tr>
													<td>Item Four</td>
													<td>Vitae integer tempus condimentum.</td>
													<td>19.99</td>
												</tr>
												<tr>
													<td>Item Five</td>
													<td>Ante turpis integer aliquet porttitor.</td>
													<td>29.99</td>
												</tr>
											</tbody>
											<tfoot>
												<tr>
													<td colspan="2"></td>
													<td>100.00</td>
												</tr>
											</tfoot>
										</table>
									</div>

									<h4>Alternate</h4>
									<div class="table-wrapper">
										<table class="alt">
											<thead>
												<tr>
													<th>Name</th>
													<th>Description</th>
													<th>Price</th>
												</tr>
											</thead>
											<tbody>
												<tr>
													<td>Item One</td>
													<td>Ante turpis integer aliquet porttitor.</td>
													<td>29.99</td>
												</tr>
												<tr>
													<td>Item Two</td>
													<td>Vis ac commodo adipiscing arcu aliquet.</td>
													<td>19.99</td>
												</tr>
												<tr>
													<td>Item Three</td>
													<td> Morbi faucibus arcu accumsan lorem.</td>
													<td>29.99</td>
												</tr>
												<tr>
													<td>Item Four</td>
													<td>Vitae integer tempus condimentum.</td>
													<td>19.99</td>
												</tr>
												<tr>
													<td>Item Five</td>
													<td>Ante turpis integer aliquet porttitor.</td>
													<td>29.99</td>
												</tr>
											</tbody>
											<tfoot>
												<tr>
													<td colspan="2"></td>
													<td>100.00</td>
												</tr>
											</tfoot>
										</table>
									</div>
								</section>

								<section>
									<h3 class="major">Buttons</h3>
									<ul class="actions">
										<li><a href="#" class="button primary">Primary</a></li>
										<li><a href="#" class="button">Default</a></li>
									</ul>
									<ul class="actions">
										<li><a href="#" class="button">Default</a></li>
										<li><a href="#" class="button small">Small</a></li>
									</ul>
									<ul class="actions">
										<li><a href="#" class="button primary icon solid fa-download">Icon</a></li>
										<li><a href="#" class="button icon solid fa-download">Icon</a></li>
									</ul>
									<ul class="actions">
										<li><span class="button primary disabled">Disabled</span></li>
										<li><span class="button disabled">Disabled</span></li>
									</ul>
								</section>

								<section>
									<h3 class="major">Form</h3>
									<form method="post" action="#">
										<div class="fields">
											<div class="field half">
												<label for="demo-name">Name</label>
												<input type="text" name="demo-name" id="demo-name" value="" placeholder="Jane Doe" />
											</div>
											<div class="field half">
												<label for="demo-email">Email</label>
												<input type="email" name="demo-email" id="demo-email" value="" placeholder="jane@untitled.tld" />
											</div>
											<div class="field">
												<label for="demo-category">Category</label>
												<select name="demo-category" id="demo-category">
													<option value="">-</option>
													<option value="1">Manufacturing</option>
													<option value="1">Shipping</option>
													<option value="1">Administration</option>
													<option value="1">Human Resources</option>
												</select>
											</div>
											<div class="field half">
												<input type="radio" id="demo-priority-low" name="demo-priority" checked>
												<label for="demo-priority-low">Low</label>
											</div>
											<div class="field half">
												<input type="radio" id="demo-priority-high" name="demo-priority">
												<label for="demo-priority-high">High</label>
											</div>
											<div class="field half">
												<input type="checkbox" id="demo-copy" name="demo-copy">
												<label for="demo-copy">Email me a copy</label>
											</div>
											<div class="field half">
												<input type="checkbox" id="demo-human" name="demo-human" checked>
												<label for="demo-human">Not a robot</label>
											</div>
											<div class="field">
												<label for="demo-message">Message</label>
												<textarea name="demo-message" id="demo-message" placeholder="Enter your message" rows="6"></textarea>
											</div>
										</div>
										<ul class="actions">
											<li><input type="submit" value="Send Message" class="primary" /></li>
											<li><input type="reset" value="Reset" /></li>
										</ul>
									</form>
								</section>

							</article> -->

					</div>

				<!-- Footer -->
					<footer id="footer">
						<p class="copyright">&copy; INSIGHT HUNTERS Bootcamp: <!--<a href="https://html5up.net">HTML5 UP</a>-->.</p>
					</footer>

			</div>

		<!-- BG -->
			<div id="bg"></div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>

	</body>
</html>

"""

components.html(html_code, height=300)
