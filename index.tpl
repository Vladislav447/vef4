<h1>Verkefni 4 - JSON</h1>

% for i in gogn['results']:
	<h3>{{i['longName']}}</h3>
	<h3>{{i['shortName']}}</h3>
	<h3>{{i['value']}}</h3>
% end