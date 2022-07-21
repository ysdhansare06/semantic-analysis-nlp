import spacy
import pandas as pd
nlp = spacy.load('en_core_web_sm')

doc=nlp("""Biology in essence is the story of life on earth. While individual
organisms die without fail, species continue to live through
millions of years unless threatened by natural or anthropogenic
extinction. Reproduction becomes a vital process without
which species cannot survive for long. Each individual leaves
its progeny by asexual or sexual means. Sexual mode of
reproduction enables creation of new variants, so that survival
advantage is enhanced. This unit examines the general
principles underlying reproductive processes in living organisms
and then explains the details of this process in flowering plants
and humans as easy to relate representative examples. A related
perspective on human reproductive health and how
reproductive ill health can be avoided is also presented to
complete our understanding of biology of reproduction.""")

tokens=[]
sents=[]
pos=[]
verbs=[]
aux=[]
ners=[]
deps=[]

# task: finding the verb in each sentence  --> printing what is left to the verb and what is right to the verb --> (left,verb,right)

for sent in doc.sents:
    sents.append(sent.text)

sentences=[]
for sent in sents:
    sentences.append(sent.replace("\n"," "))

for sent in sentences:
    doc=nlp(sent)
    for token in doc:
        tokens.append(token.text)
        pos.append(token.pos_)
        deps.append(token.dep_)
        
        if token.pos_=='VERB' or token.pos_=='AUX':
            verbs.append(token.text)
         
newverbs=[]

for i in verbs:
    if i not in newverbs:
        newverbs.append(i)

lverb=[]
rverb=[]
for sent in sentences:
    for verb in newverbs:
        doc=nlp(sent)
        for token in doc:
            if verb == token.text:
                ind=sent.index(verb)
                left=sent[:ind]
                lverb.append(left)
                right=sent[ind+len(verb)+1:]
                rverb.append(right)
  

dict = {'Left to Verb':lverb, 'verb':verbs, 'Right to verb':rverb}
df = pd.DataFrame(dict)
df.to_csv('lvr.csv')

