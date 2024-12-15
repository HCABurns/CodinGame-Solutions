Link to Submission: [GeoGuessr Best Guess](https://www.codingame.com/contribute/view/111588c1aaba588f0c2ec3275a5095b166aa45)

## Context

In NMPZ GeoGuessr, players analyse an image for clues such as road markings, domain names, vehicle licence plates, and other visual indicators. Using these clues, players must attempt to pinpoint the exact location where the image was taken. As this is not possible in CodinGame, the country name can be used instead. Players are given a list of information about the clues of a given image as well as a list of candidate countires. The candidate countries includes the country name as well as information regarding that couuntry. Players must match information from the clues to the information about a country and determine the best guess. The best guess is the country that has the most matches to the clues found in the image.

## Information

The image given is a google image still image and can be anywhere, with google coverage, in the 107 countries in the game. This can be an urban or rural setting, in any season and any time of the day. Some commom information that can be gathered is:

Road lines - Shape and colours can be used to identify countries.

License plates (front and rear) - License plates vary in colours and sizes of countries so can be helpful.

Domain - Domain are extremely helpful as 99.9% of the time a domain, excluding .com, can instantly be used identify the country.

Telephone number - Telephone numbers can be used to identify countries and could be used for region guessing.

## Example

bollard-white:road lines-white

7

Japan:driving side-left:bollard-white:front licence plate-white:rear licence plate-white:telephone-+81:language-Japanese

Spain:road lines-white:domain-.es:language-Spanish:rear licence plate-EU:front licence plate-EU:telephone-+34:driving side-right

Portugal:road lines-white:domain-.pt:rear licence plate-yellow bar:front licence plate-yellow bar:telephone-+351:driving side-right

France:road lines-white:language-French:telephone-+33:domain-.fr:bollard-white:driving side-right

Malta:driving side-left:road lines-white:front licence plate-EU:rear licence plate-EU:domain-.mt:telephone-+356

Norway:domain-.no:language-Norwegian:front licence plate-white:rear licence plate-white:driving side-right:telephone-+47

Sweden:domain-.se:telephone-+46:language-Swedish:driving side-right:telephone-+46:road lines-white:rear licence plate-EU:front licence plate-EU

Japan: 1 matches
Spain: 1 matches
Portugal: 1 matches
France: 2 matches
Malta: 1 matches
Norway: 0 matches
Sweden: 1 matches

### Result 
Therefore, France is the best guess as it has the most matches. (In the event France also had 1 match, Japan would be the best guess as it has a higher precedence)

