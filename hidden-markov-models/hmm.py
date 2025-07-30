from decimal import *

ctx = Context(prec=4, rounding=ROUND_DOWN)
setcontext(ctx)

string_seq = []
states_observables = []
pair_values = []
cases = []
cases_answers = []

transition_prob = {}
prob_n = {}

def loadData():
    input_reader = open('data/hmm.in', 'r')

    str_count = int(input_reader.readline().strip())        #

    for i in range(str_count):
        string_seq.append(input_reader.readline().strip())
    #values and observables
    state = []
    for s in input_reader.readline().strip().split(" "):
        state.append(s)
    states_observables.append(state)
    
    observables = []
    for o in input_reader.readline().strip().split(" "):
        observables.append(o)
    states_observables.append(observables)

    _s = []
    for p in input_reader.readline().strip().split(" "):
        _s.append(Decimal(p))
    pair_values.append(_s)

    _t = []
    for v in input_reader.readline().strip().split(" "):
        _t.append(Decimal(v))
    pair_values.append(_t)
    
    case_count = int(input_reader.readline().strip())
    for i in range(case_count):
        case = []
        for c in input_reader.readline().strip().split(" "):
            case.append(c)
        cases.append(case)

    input_reader.close()

def computeTransitionP(ss):
    global transition_prob
    #match pair values with states and observables
    for s in states_observables[0]:
        for o in states_observables[1]:
            transition_prob.update({o+s : pair_values[states_observables[0].index(s)][states_observables[1].index(o)]})
    
    #populate state transition
    new = []
    for i in range(len(ss)-1):
        k = ss[i+1]+ss[i] #__ given __ format
        if k in transition_prob:
            transition_prob.update({k : transition_prob.get(k) + 1})
        else:
            new.append(k)
            transition_prob[k] = 1
    #compute transition probabilities of states
    for i in new:
        transition_prob.update({ i :  (Decimal(str(transition_prob.get(i))) / Decimal(str(ss[0:-1].count(i[1])))) })

def computeTotalP_state(Sn):
    s = Sn[0]
    n = int(Sn[-1])

    if s + str(n-1) not in prob_n:
        computeTotalP_state(s + str(n-1))
    else:
        ans = Decimal('0.0')
        for i in states_observables[0]:
            t = s+i
            ans = ans + (transition_prob.get(t) * prob_n.get(i+str(n-1)))
        prob_n.update({ Sn : ans })

        for i in states_observables[0]:
            if (s != i) and (i + str(n) not in prob_n):
                prob_n.update({ i + str(n) : Decimal(str(1-ans)) })
        
def computeTotalP_obsrv(Sn):
    s = Sn[0]
    n = int(Sn[-1])

    ans = Decimal('0.0')
    for i in states_observables[0]:
        t = s+i
        if(i + str(n) not in prob_n): computeTotalP_state(i + str(n))
        ans = ans + (transition_prob.get(t) * prob_n.get(i + str(n)))
    prob_n.update({ Sn : ans })

def bayesRule(A, B):
    # A|B = (P(B|A) * P(A)) / P(B)
    pba = transition_prob.get(B[0] + A[0])
    pa = prob_n.get(A)
    pb = prob_n.get(B)

    return ((pba * pa) / pb)

def fileOutput():
    output_writer = open('hmm.txt', 'w')

    for i in range(len(string_seq)):
        output_writer.write(string_seq[i] + "\n")

        for c in range(len(cases)):
            for cc in cases[c]:
                output_writer.write(cc + " ")
            output_writer.write(str(cases_answers[i][c]) + "\n")
    
    output_writer.close()
#MAIN
loadData()

for ss in string_seq:
    for s in states_observables[0]:   #'S'
        if ss[0] == s:
            prob_n.update({ s+'0' : Decimal('1.0') })
        else:
            prob_n.update({ s+'0' : Decimal('0.0') })
        
    computeTransitionP(ss)
    
    ca = []
    for c in cases:
        if c[0] not in prob_n:
            if c[0][0] in states_observables[0]:
                computeTotalP_state(c[0])
            else:
                computeTotalP_obsrv(c[0])

        if c[-1] not in prob_n:
            if c[-1][0] in states_observables[1]:
                computeTotalP_obsrv(c[-1])
            else:
                computeTotalP_state(c[-1])

        
        ans = bayesRule(c[0],c[-1])
        ca.append(ans)
    cases_answers.append(ca)
    transition_prob.clear()
    prob_n.clear()
fileOutput()