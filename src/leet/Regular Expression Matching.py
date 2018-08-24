# coding: utf8
"""
---------------------------------------------
    File Name: Regular Expression Matching.py
    Description: 
    Author: wangdawei
    date:   2018/1/11
---------------------------------------------
    Change Activity: 
                    2018/1/11
---------------------------------------------    
"""

import re


class Patt(object):
    def __init__(self, c, star=False):
        self.c = c
        self.star = star
        self.l = len(c)

    def __repr__(self):
        return "[%s, %s, %s]" % (self.c, self.star, self.l)


class Solution(object):
    def __init__(self):
        pass


    def t(self):
        pass


    def find_first_str(self, ps):
        for i in range(len(ps)):
            if not ps[i].star:
                return i
        return -1


    def isMatch_char(self, s1, s2):
        if len(s1) != 1 or len(s2) != 1:
            return False
        elif s2 == ".":
            return True
        elif s1 == s2:
            return True
        else:
            return False

    def isMatch_string(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for s1e, s2e in zip(s1, s2):
            if not self.isMatch_char(s1e, s2e):
                return False
        return True

    def isMatch_rec(self, s, ps):

        ls, lps = len(s), len(ps)
        pd = {}
        for k, v in zip(["has_str", "has_dot", "has_sstar", "has_dstar", "has_star"],
                        [False, False, False, False, False]):
            pd[k] = v
        for pe in ps:
            if pe.star:
                pd["has_star"] = True
                if pe.c == ".":
                    pd["has_dstar"] = True
                else:
                    pd["has_sstar"] = True
            else:
                if pe.c.find(".") >= 0:
                    pd["has_dot"] = True
                for c in pe.c:
                    if c != ".":
                        pd["has_str"] = True

        print("#" * 50)
        print(s, ps, pd)
        # not has_star
        if not pd["has_star"]:
            print("# not has_star")
            ps_str = "".join([pe.c for pe in ps])
            if len(s) != len(ps_str):
                return False
            else:
                return self.isMatch_string(s, ps_str)
        # only has_sstar, str star
        elif not pd["has_str"] and not pd["has_dot"] and pd["has_sstar"] and not pd["has_dstar"]:
            print("# only has_sstar")
            i, j = 0, 0
            while i < ls:
                while j < lps:
                    if self.isMatch_char(s[i], ps[j].c):
                        # i += 1
                        while i < ls and self.isMatch_char(s[i], ps[j].c):
                            i += 1
                        j += 1
                        break
                    j += 1
                if j == lps:
                    break
            if i == ls:
                return True
            else:
                return False
            pass
        # only has_dstar, dot star
        elif not pd["has_str"] and not pd["has_dot"] and not pd["has_sstar"] and pd["has_dstar"]:
            print("# only has_dstar, dot start")
            return True
            pass
        # has str or star, has str star,
        elif not ps[0].star:
            print("ps 0 not star")
            if self.isMatch_string(s[0:ps[0].l], ps[0].c):
                return self.isMatch_rec(s[ps[0].l:], ps[1:])
            else:
                return False
        elif not ps[-1].star:
            print("ps -1 not star")
            if self.isMatch_string(s[-ps[-1].l:], ps[-1].c):
                return self.isMatch_rec(s[:-ps[-1].l], ps[:-1])
            else:
                return False
        else:
            print("string in middle")
            first = self.find_first_str(ps)
            pp = ps[first]
            for inds, inde in [(m.start(), m.start()+pp.l) for m in re.finditer(pp.c, s)]:
                if self.isMatch_rec(s[:inds], ps[:first]) and self.isMatch_rec(s[inde:], ps[first+1:]):
                    return True
            return False

            pass


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # replace repeat stars to a star, find star' char index
        print("#" * 80)
        p_org = p
        p = p_org.lstrip("*")
        p = re.sub("\*{2,}", "*", p)
        print(p)
        ls, lp, star_inds = len(s), len(p), [m.start() for m in re.finditer('\*', p)]
        print("star_inds", star_inds)

        # pattern string to pattern patt

        c_inds = [i - 1 for i in star_inds]
        c_inds_set = set(c_inds)
        i = 0
        ps = []
        while i < lp:
            if i not in c_inds_set:
                ps.append(Patt(p[i]))
                i += 1
            else:
                ps.append(Patt(p[i], True))
                i += 2
        print("patt", ps)

        # dot star and str star sequence to a dot star
        pso = ps
        ps = []
        i = 0
        last_star, tmp_ps, dstar = None, [], False
        tmp_ss = []
        # process pstar seq
        while i < len(pso):
            pe = pso[i]
            if pe.star == False:
                # process pstar seq
                if last_star == True:
                    if  dstar == False:
                        ps.extend(tmp_ps)
                    else:
                        ps.append(Patt(".", True))
                        dstar = False
                    tmp_ps = []
                tmp_ss.append(pe.c)
                last_star = False
            else:
                if last_star == False:
                    ps.append(Patt("".join(tmp_ss)))
                    tmp_ss = []
                if pe.star == True and pe.c == ".":
                    dstar = True
                tmp_ps.append(pe)
                last_star = True
            i += 1

        if last_star == True:
            if dstar == False:
                ps.extend(tmp_ps)
                tmp_ps = []
            else:
                ps.append(Patt(".", True))
                dstar = False
        else:
            ps.append(Patt("".join(tmp_ss)))
            tmp_ss = []
        print("str star dot star sequence combine to dot star", ps)

        return self.isMatch_rec(s, ps)


def main():
    solution = Solution()
    # solution.isMatch("aa", "a")
    # exit(-1)
    # solution.isMatch("aa", "aa")
    # solution.isMatch("aaa", "aa")
    # solution.isMatch("aa", "a*")
    # solution.isMatch("aa", ".*")
    # solution.isMatch("ab", ".*")
    # solution.isMatch("aab", "c*a*b")

    assert (solution.isMatch("a", "ab*a") == False)
    assert (solution.isMatch("ab", ".*..") == True)
    assert (solution.isMatch("aa", "a") == False)
    assert (solution.isMatch("aa", "aa") == True)
    assert (solution.isMatch("aaa", "aa") == False)
    assert (solution.isMatch("aa", "a*") == True)
    assert (solution.isMatch("", ".*") == True)
    assert (solution.isMatch("aa", ".*") == True)
    assert (solution.isMatch("ab", ".*") == True)
    assert (solution.isMatch("ab", ".*b.*") == True)
    assert (solution.isMatch("abab", ".*b.*") == True)
    assert (solution.isMatch("abab", ".*b.*b") == True)
    assert (solution.isMatch("abab", ".*ba*.*a*b") == True)
    assert (solution.isMatch("ababc", ".*ba*.*a*b") == False)
    assert (solution.isMatch("abab", ".*ba*.*a*") == True)
    assert (solution.isMatch("abab", ".*ba*.*a*c") == False)
    assert (solution.isMatch("abab", ".*ba*.*a*c.*") == False)
    assert (solution.isMatch("abab", ".*ba*.*a*b") == True)
    assert (solution.isMatch("", "a*a*a*") == True)
    assert (solution.isMatch("a", "a*a*a*") == True)
    assert (solution.isMatch("b", "a*b*a*") == True)
    assert (solution.isMatch("aab", "c*a*b") == True)
    assert (solution.isMatch("aab", "c*a*b") == True)
    assert (solution.isMatch("aab", "c*a*b") == True)


if __name__ == "__main__":
    main()
