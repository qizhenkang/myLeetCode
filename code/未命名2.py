# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 10:55:46 2021

@author: Zhenkang
"""

class Solution:
    def countVowels(self, word: str) -> int:
        
        # vowelDict = {'a':0,
        #             'e':0,
        #             'i':0,
        #             'o':0,
        #             'u':0}
        vowelSet = {'a','e','i','o','u'}

        N = len(word)
        nums = [False]*N
        volNum = 0
        for i in range(N):
            if word[i] in vowelSet:
                nums[i] = True
                volNum +=1
        dp = [0] * (N+1)
        dp[1] = 1 if nums[0] else 0
        for i in range(2,N+1):
            if nums[i-1]:
                dp[i] = dp[i-1] * 2 - dp[i-2] + i 
            else:
                dp[i] = dp[i-1] * 2 - dp[i-2]
        return dp[N]
        
        # print(nums)
        # # print(volNum)
        # result = 0
        # 找连续
        # state = 0
        # result = 0
        # connum = 0
        # for i in range(N):
        #     if nums[i]:
        #         connum += 1
        #     else:
        #         if connum:
        #             result +=
        #         connum = 0
        
        
        # for length in range(1,N+1):
        #     vowelNum = 0
        #     for i in range(N-length+1):
        #         if i == 0:
        #             for k in range(i,i+length):
        #                 if nums[k]:
        #                     vowelNum +=1
        #         else:
        #             if nums[i-1]:
        #                 vowelNum -=1
        #             if nums[i+length-1]:
        #                 vowelNum +=1
        #         result += vowelNum

        # return result

if __name__ == '__main__':
    solu = Solution()
    arr = [1,3,5,7,8]
    difference = 1
    nums = [9,6,4,2,3,5,7,0,1]
    nums = [1]
    # nums = [2,7,4,5,9,0,6,8,3]
    nums = 'noosabasboosa'
    # nums = "cwndkkjywbrctsmrbcfspuyiswhroqzsxqwwgxskffpmwubdrcxowtcimldmagoixeaejweszgxvzfoqtovhznhznssdjkwjvjyyraobwkugmrhdiltvuuijrjixbnfofzhafamoftbsdwqoigcdwswasgntrqhnarnuamhdtbltgzbwpxkhbatwbimudfyivkfxkddpzxrtyhqirrdbubudfmuakzjrbdoqlusrjwncihusgwetkquiilenutqxbceznyvyndcqryjkofyjwaicsnxqzoevtnsucopkezzennifztwkzdwvbetukrldorjhieqrgfmzyqruhdxjtstzrzltrekmbsoxtbhgrbuekutxthldjjswschukgzhwpxpsfutkabokufyhhwlwkdlykpqztkkoqirbfdczeqnpfkzgegobamhylpzirzkitymjlcbbxqgxraqjpaodgmparufwrmwrprszcpoduqcdepdyncagrhjhqswkqmbpkqtmixjiuhdwfzkpgimuarpkmxmaktkhioqwyvlplspqbhainmfgjyvvsewfimceepsaeprkixdxgqxlhkpsfhzzbdchiauspzaphccraarzeoufbuhyfpfehpssrznooahzfnsafsvzqudaefmkhoilodjwygzyrymjfbqtvpvmmbntgsxkvlunzqpmxpnaedfzlzurghgmiiszlmgsayfsdjxflcwnltujaldudkhmgrumeasmsezutsbagxrzthpifbyepgmirjiimileyawxsmifbbzlomfakzfocbukvehdvcrxkmxduwlvxxuummrxqjysgkwffcpmnpnisbtczlcdvxeknwdmqllzqqasiobubtkrgvtvwkrqnolytmkwlhvmojhsalrrgzquxfmtqyvhlivhzkbrncvsxcarjiicttkczndongnsqegpkmxafzolcrcmjlyyrpowznijkvweacxkxzmsuqqkxfeuqwuckszcggiunfevtyvncqxdbxogicuprgcnnudmpuqwwdwztzgpuxacqnortueqrskwnaxcviqpaxbpbhwmgkufujbexjcuebikmnypeiwqevajobzyubvabozauxnpxkiqiblxvdmgyadpdoqshhguopzrnoyuvgkwufjidjwzchfpqralydfhckswyvwrcjogkzajvsckthsuapwipcmeuogjuxlwazyzjrufkpzsvbsooirnxbrnbivuwiteillhflyvrkiwjtbtbfxlqfppedhkrmdfvmmpofqekdjcypaghrpjalwzhecgbpdhwogdtycvejfkddnioafbjiybnwzmzftczynmbhyhiupdgosqpkfnncwkjthpxleypbxnxsiqcjlaffxyvdqgbgktkpupvtkcipmfzpcnovngqgxisxyspcbhorsfjluheirvtljlflnjgxvjxttxwfgmmtzdglcylefxdtnuiddbwnbrhmwfnmwpkkqmgiultoaubtbnukmyyrsahvbkkeanusfxvqlfalhgmxovbjupbwfoyxbzxcalnuaftdsgazpegkzdzlkuuirfuaauocxbquoaxqpxhffwwdfuyunbpkntwmsbapwhutfzqeqhllilrhvviletbhgayytbvpuzeehbolmytonttkehmlrrtfxdhhklzjjrkqxuhkmkwmfbwgzwddqahdifnpzxcuvsuvoopjeabmwqspumzighryhfqgtwssxfckrlwjpgtuvqcsosuvbcolxapenaartjhewhtktzecljjzjicjiqzoadbevqglqcddbxudwbtrnriaxpibjmyphqrpavtueigwtrhufiofqobjqcwdnaxffkanrgxcszpikayrhibxvxthcmoftxcrgeoxnowowtvnpqyuguehnlatmiyzkpaxbbmrahynouwptpjjdvmbndebkyujccesbqrdnqrteiqsjkamdzgggokodcvjjezdrcmfanefqxdldbqyfjcskhrtxoktfxueuqomztysetglxcjpxhoxcfvoxhdgotastdertigpzygnjrbkpiigykvybjytxmybltkrogvlhrufuywpvwjylyrowddhkcktjmqydpzsqkadyoxiacrjipmsbhgkoxeamoovcykwdfyxzatsxovorgviwgzheiwwhekictrnybmrnxgccyvesscuckltwthhnrziycmpwivrvbtgrdhminlbmtwtfxhimxysthjtwcxlmwjphnywyvaoqattrvhlkbsonhgcolmpmavwtktmkusvmawhwoswjhqfkwqrhxmefldqawpzybhaetjityrbotpliibxvoncihevdbhkxvrhnuyunsjcuyntgysrandvzgddmxpdhgupuuzhgxhmqgkkrkmtbbtjmxdqfkxoyouoqnkwjankppozzxfskrqlreqttizkpowivqasnlhfmmmjpaxgqmivafpcjsxgcxatzwjejkfmwihmnclqvyvsemjneufpxvyiyilejadgajpkpqkcjvctkwzyjpfslqjjoadznjqklakpfyupxjtrslkqltmsafzjpyuawaqliebfvskkosoxuietoelqmvmguoysreswrlsrjwxdsvkguqhqayetyfrzgjgofzajtttrqevlahkwxmzgrhjqngcamqeqsjvwrgfqtnxgpdqvgctegdwgsmszfkxzjdwpibivkqrhanavwdxgrpcrwpgxyygwmvatxkynybyvdkozlpgsshqikllokryusspagoifrshqjbasraqpnbaozhpqjvjomzxwzvldssjylanqkuafdxefoyveyouilkhigxyyjxsojoacwjswnbmqgyhygjxnsvaymyzhoomtprnvfrcxcqxeefhuseaqqvdbxrcgkelaqofewppmanusbpglwulifuvpqckqoxkkanbuupkrarmbdpwjomkpagrkorfedqymlanhmqogocgxxxwabrtknqxcgqwuotlwvmyrulhwsrsypxicxlvgpkouewfwyjovlbfkfbxhgkfjajwwwpcdtgjzqdlunabgfnjwkxlfopnjhiiuipasiqusexrkypftyxowxqvbsqwwcxhptrtaflzntkolrjrgvuzhbxjgilzjuqrxvajfkkbbtlmuyavlndmmebtjrorzvidrrehyqswhzzeuycgjuylzveajtevfwomsdfcvbqmtixbtfrzwegsldjzjqkktfxoslxrhkvtudmxmiouaphzwfazxgeqbhiqbuzhwyjlvpqyumrfaetgmavbmkfwhmwooujpevbkxhdvqacrjcuntqqkcisefoaflpscenpojwrnsilxisxyroujchgpavggcabmvixmnxrejhtaeqfpkqkzhavgbdnipxpmskhfbnormjopacsslalvbjsjleduwlvvuirqzyjftwccjlrqrwkikbipxmjfzncykmttjpuoggfrwpjoprumxxnudmeduirjwozxkncfgpouacrveprnullcmrvchypjkwsnvjkidoihpwfgoudjgrwqfzkuewudlunrbhvyblyfxbnbwccjqrfqrsxschwyomlmdlocsjqiofwvcrywriphpgkvvfikmirzdudwaubrnsdmesghqztngbrosmnuglxbgwarhyurnovntfsfaxbyiuqxihwguckrtqyqvbenerhrylzjyiuaqavwmkiteopyhjlmxxaxhnkqwtikcuadwdewmvvkawrimdzsfrnnjasagmlaxucwcphwztsnbhkpsinfykqsoymypextywhkzpjvbleiwdhwotddegtulmznhrjjdfltumcnlhosmeqnpyrjfdytqtgeclqyruiqsmzlkfqdqzvmovezaimorkeznfuncegurrrgjbanrirwrtnhrdowihsfzpprfjaychistbdjxiseavcihwwetfxvlvmttqvomkvsjyctmsipuuduprciflwskotkqkavujbjkgmtjuapqhqpumkxwjkkgabjwjocxysoqsqbxiakjtptpuwoxnzsjxhzyqqcrtwizqbuahstkjzxellajsnzfapgjpqzodnuodlktqkeniuriiovarkleyannwcxmsetvdzcjwiafvutwjtzvkxnzufzhiqfwvxwfpnntkcmrjnbfnpdwfmhedtsfwwflrmudcyfdxhbbcrgvhgoeakmtsnpwcwuvgcshqqgfluwqiqmanouxjtkzgbeqhilbpbplovxchiznfunkfhybjtfbocrmgzjiexjmvhcwxsmtsugdgfnweiqifbjkfotyhqgtsnvqjslcqbmvteavougtptiahjqfdqwwmmhlatpamndhiexsbfhhnsvldqmdixtrflperlxnatvbrnkkopqvsjyzrdqtwcpkxsjhsmkvapcwxfpabbibmsatwcgtymvdhgycrbjotmkelhevulwgezziicmvrahwucbjozvyixveikpdwtjtgpuvsgxsmxzazjcaoznkdxsfgdxlbkqwmdprkddisqdvoytorycire"
    # difference = 1
    output_Str = 'result = ' + str(solu.countVowels(nums))
    print(output_Str)