grammar NTUFPI;

noticia: paragrafo+ EOF;
paragrafo: frase+ '\n'*;
frase: (ARTIGO | PALAVRA | DIA_DA_SEMANA | MES | HORARIO | ADVERBIO | PORCENTAGEM | PONTUACAO | SIGLA | NOME_PROPRIO | DINHEIRO | ESTADO | NUMERO | DATA | ABREVIACAO)* PONTO_FINAL;

ESTADO: A M A P A | A M A Z O N A S | P A R A | R O R A I M A | A C R E | R O N D O N I A | M A R A N H A O | P I A U I | S E R G I P E | P E R N A M B U C O | A L A G O A S | C E A R A |
        R I O [ ] G R A N D E (D O [ ] N O R T E | D O [ ] S U L) | B A H I A | P A R A I B A | E S P I R I T O [ ] S A N T O | R I O [ ] D E [ ] J A N E I R O | S A O [ ] P A U L O |
         M I N A S [ ] G E R A I S | T O C A N T I N S | G O I A S | M A T O [ ] G R O S S O ([ ] D O [ ] S U L)? | P A R A N A | S A N T A [ ] C A T A R I N A | D I S T R I T O [ ] F E D E R A L
         A C | A L | A P | A M | B A | C E | D F | E S | G O| M A | M T | M S| M G | P A | P B | P R | P E | P I | R R | R O | R J | R N | R S | S C | S P | S E | T O;
SIGLA: ([A-Z&][A-Z&]+);
ARTIGO: O | A | O S | A S | U M | U M A | U N S | U M A S;
NUMERO: [0-9]+;
DIA_DA_SEMANA: D O M I N G O | S E G U N D A ('-' F E I R A)?| T E R C A ('-' F E I R A)?| Q U A R T A ('-' F E I R A)?| Q U I N T A ('-' F E I R A)?| S E X T A ('-' F E I R A)?| S A B A D O |
               D O M | S E G | T E R | Q U A | Q U I | S E X | S A B;
MES: J [aA] N [eE] [iI] R [oO] |F [eE] V [eE] R [eE] [iI] R [oO] | M A R C O | A B R I L | M A I O | J U N H O | J U L H O | A G O S T O | S E T E M B R O | O U T U B R O | N O V E M B R O | D E Z E M B R O
    | J A N | F E V | M A R | A B R | M A I | J U N | J U L | A G O | S E T | O U T | N O V | D E Z;
HORARIO: (NUMERO ':' NUMERO) | NUMERO [hH] NUMERO? (M [iI] N)?;
DATA: (NUMERO '/' NUMERO ('/' NUMERO)?);
ADVERBIO: [a-zA-ZáÁàÀâÂãÃçÇéÉêÊíÍóÓõÕôÔúÚ]+ 'mente';
PORCENTAGEM: NUMERO '%';
PONTUACAO: ',' | ':' | ';' | '...' | '"' | '?' | '!' | '(' | ')' | '[' ']' | '{' '}' | '/' | '“' | '”';
ABREVIACAO: [a-zA-Z][a-zA-Z][a-zA-Z]?[a-zA-Z]? '.' ' ';
PONTO_FINAL: '.';
DINHEIRO: UNIDADE_MONETARIA [ ]? NUMERO;
NOME_PROPRIO: ([A-Z][a-zA-ZáÁàÀâÂãÃçÇéÉêÊíÍóÓõÕôÔúÚ]+ ([ ] NOME_PROPRIO)?);
PALAVRA: [a-zA-ZáÁàÀâÂãÃçÇéÉêÊíÍóÓõÕôÔúÚ0-9-]+;
Space: [ \t\r\n] -> skip;

fragment UNIDADE_MONETARIA: '$' | 'R$' | '€';
fragment A : [aAáÁàÀâÂãÃ];
fragment B : [bB];
fragment C : [cCçÇ];
fragment D : [dD];
fragment E : [eEéÉ];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iIíÍ];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oOóÓõÕôÔ];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uUúÚ];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];
//fragment LETRAS_ACENTUADAS : 'á' |'à'|'â'|'ã'|'é'|'ê'|'í'|'ó'|'ô'|'õ'|'ú'|'ç'|'À'|'Á'|'Â'|'Ã'|'É'|'Ê'|'Í'|'Ó'|'Ô'|'Õ'|'Ú'|'Ü'|'Ç';