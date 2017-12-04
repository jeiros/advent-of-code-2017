"""
http://adventofcode.com/2017/day/1
"""


def captcha_sum(puzzle):
    output = 0
    for num, next_one in zip(puzzle, puzzle[1:]):
        if num == next_one:
            output += int(num)
    if puzzle[0] == puzzle[-1]:
        output += int(puzzle[0])
    return output


def captcha_halfway(puzzle):
    puzzle_dbl = puzzle * 2
    step = int(len(puzzle) / 2)

    output = 0

    for i in range(len(puzzle)):
        if puzzle[i] == puzzle_dbl[i + step]:
            output += int(puzzle[i])
    return output


assert captcha_sum('1122') == 3
assert captcha_sum('1111') == 4
assert captcha_sum('1234') == 0
assert captcha_sum('91212129') == 9


assert captcha_halfway('1212') == 6
assert captcha_halfway('1221') == 0
assert captcha_halfway('123425') == 4
assert captcha_halfway('123123') == 12
assert captcha_halfway('12131415') == 4

if __name__ == '__main__':
    puzzle = '77736991856689225253142335214746294932318813454849177823468674346512426482777696993348135287531487622845155339235443718798255411492778415157351753377959586612882455464736285648473397681163729345143319577258292849619491486748832944425643737899293811819448271546283914592546989275992844383947572926628695617661344293284789225493932487897149244685921644561896799491668147588536732985476538413354195246785378443492137893161362862587297219368699689318441563683292683855151652394244688119527728613756153348584975372656877565662527436152551476175644428333449297581939357656843784849965764796365272113837436618857363585783813291999774718355479485961244782148994281845717611589612672436243788252212252489833952785291284935439662751339273847424621193587955284885915987692812313251556836958571335334281322495251889724281863765636441971178795365413267178792118544937392522893132283573129821178591214594778712292228515169348771198167462495988252456944269678515277886142827218825358561772588377998394984947946121983115158951297156321289231481348126998584455974277123213413359859659339792627742476688827577318285573236187838749444212666293172899385531383551142896847178342163129883523694183388123567744916752899386265368245342587281521723872555392212596227684414269667696229995976182762587281829533181925696289733325513618571116199419759821597197636415243789757789129824537812428338192536462468554399548893532588928486825398895911533744671691387494516395641555683144968644717265849634943691721391779987198764147667349266877149238695714118982841721323853294642175381514347345237721288281254828745122878268792661867994785585131534136646954347165597315643658739688567246339618795777125767432162928257331951255792438831957359141651634491912746875748363394329848227391812251812842263277229514125426682179711184717737714178235995431465217547759282779499842892993556918977773236196185348965713241211365895519697294982523166196268941976859987925578945185217127344619169353395993198368185217391883839449331638641744279836858188235296951745922667612379649453277174224722894599153367373494255388826855322712652812127873536473277'
    print(captcha_sum(puzzle))
    print(captcha_halfway(puzzle))
