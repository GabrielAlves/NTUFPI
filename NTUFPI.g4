grammar NTUFPI;

noticia: paragrafo+ EOF;
paragrafo: frase+ '\n'*;
frase: (ARTIGO | PALAVRA | DIA_DA_SEMANA | MES | HORARIO | ADVERBIO | PORCENTAGEM | PONTUACAO | SIGLA | NOME_PROPRIO | DINHEIRO | ESTADO | NUMERO | DATA | ABREVIACAO | ABREVIACAO | PREPOSICAO | PRONOME | CIDADE | TEMPO | CONJUNCAO)* PONTO_FINAL;

CIDADE : T E R E S I N A | P I C O S;
ESTADO: A M A P A_AGUDO | A M A Z O N A S | P A R A_AGUDO | R O R A I M A | A C R E | R O N D O_CIRCUNFLEXO N I A | M A R A N H A_TIL O | P I A U I_AGUDO | S E R G I P E | P E R N A M B U C O | A L A G O A S | C E A R A_AGUDO |
        R I O [ ] G R A N D E (D O [ ] N O R T E | D O [ ] S U L) | B A H I A | P A R A I_AGUDO B A | E S P I R I T O [ ] S A N T O | R I O [ ] D E [ ] J A N E I R O | S A_TIL O [ ] P A U L O |
         M I N A S [ ] G E R A I S | T O C A N T I N S | G O I A_AGUDO S | M A T O [ ] G R O S S O ([ ] D O [ ] S U L)? | P A R A N A_AGUDO | S A N T A [ ] C A T A R I N A | D I S T R I T O [ ] F E D E R A L
         A C | A L | A P | A M | B A | C E | D F | E S | G O| M A | M T | M S| M G | P A | P B | P R | P E | P I | R R | R O | R J | R N | R S | S C | S P | S E | T O;
SIGLA: ([A-Z&][A-Z&-]+);
CONJUNCAO: [ ] E [ ] | M A S | P O R T A N T O | C O N T U D O;
PREPOSICAO: A_CRASE S? | A N T E | A P O_AGUDO S | A T E_AGUDO | C O M | C O N T R A | PREPOSICAO_DE | D E S D E | PREPOSICAO_EM | E N T R E | P A R A | P E R | P E R A N T E | PREPOSICAO_POR | S E M | S O B | S O B R E | T R A_AGUDO S;
PREPOSICAO_DE: D E | D O S? | D A S?;
PREPOSICAO_EM: E M | N O S? | N A S?;
PREPOSICAO_POR: P O R | P E L O S? | P E L A S? | P R O S? | P R A S?;
ARTIGO: O | A | O S | A S | U M | U M A | U N S | U M A S;
NUMERO: [0-9]+;
PRONOME: E U | T U | V O C E | (D | N)? E L E S? | (D | N)? E L A S? | N O_AGUDO S | V O_AGUDO S | (D | N)? E S (T | S) (E | A) S?;
DIA_DA_SEMANA: D O M I N G O | S E G U N D A ('-' F E I R A)?| T E R C A ('-' F E I R A)?| Q U A R T A ('-' F E I R A)?| Q U I N T A ('-' F E I R A)?| S E X T A ('-' F E I R A)?| S A B A D O |
               D O M | S E G | T E R | Q U A | Q U I | S E X | S A B;
MES: J A N E I R O |F E V E R E I R O | M A R C_CEDILHA O | A B R I L | M A I O | J U N H O | J U L H O | A G O S T O | S E T E M B R O | O U T U B R O | N O V E M B R O | D E Z E M B R O
    | J A N | F E V | M A R | A B R | M A I | J U N | J U L | A G O | S E T | O U T | N O V | D E Z;
HORARIO: (NUMERO ':' NUMERO) | NUMERO H NUMERO? (M I N)?;
DATA: (NUMERO '/' NUMERO ('/' NUMERO)?) | NUMERO [ ] D E [ ] MES ([ ] D E [ ] NUMERO)?;
ADVERBIO: [a-zA-ZáÁàÀâÂãÃçÇéÉêÊíÍóÓõÕôÔúÚ]+ 'mente' | S I M | N A_TIL O | T A L V E Z | H O J E | O N T E M | A M A N H A_TIL | A Q U I | M U I T O | P O U C O | J A_AGUDO;
PORCENTAGEM: NUMERO '%';
PONTUACAO: ',' | ':' | ';' | '...' | '"' | '?' | '!' | '(' | ')' | '[' ']' | '{' '}' | '/' | '“' | '”' | 'º';
ABREVIACAO: [a-zA-Z][a-zA-Z][a-zA-Z]?[a-zA-Z]? '.' ' ';
PONTO_FINAL: '.';
DINHEIRO: UNIDADE_MONETARIA [ ]? NUMERO;
NOME_PROPRIO: ([A-Z][a-zA-ZáÁàÀâÂãÃçÇéÉêÊíÍóÓõÕôÔúÚ]+ ([ ] NOME_PROPRIO)?);
TEMPO: NUMERO [ ] (A N O S? | D I A S? | M E S (E S)?);
PALAVRA: [a-zA-ZáÁàÀâÂãÃçÇéÉêÊíÍóÓõÕôÔúÚ0-9-]+;
Space: [ \t\r\n] -> skip;

fragment UNIDADE_MONETARIA: '$' | 'R$' | '€';
fragment A : [aA];
fragment A_AGUDO : [áÁ];
fragment A_CRASE : [àÀ];
fragment A_CIRCUNFLEXO : [âÂ];
fragment A_TIL : [ãÃ];
fragment B : [bB];
fragment C : [cC];
fragment C_CEDILHA : [çÇ];
fragment D : [dD];
fragment E : [eE];
fragment E_AGUDO : [éÉ];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment I_AGUDO : [íÍ];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment O_AGUDO : [óÓ];
fragment O_TIL : [õÕ];
fragment O_CIRCUNFLEXO : [ôÔ];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment U_AGUDO : [úÚ];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];