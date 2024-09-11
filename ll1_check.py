from grammar import Grammar
from predict import predict_algorithm


def is_ll1(G: Grammar, pred_alg: predict_algorithm) -> bool:
    for A in G.nonterminals():
        print(f"Analisando o não-terminal: {A}")
        pred_set = set()
        for p in G.productions_for(A):
            pred = pred_alg.predict(p)
            print(f"Produção: {p} - Predições: {pred}")
            if not pred_set.isdisjoint(pred):
                print(f"Conflito detectado no não-terminal {A} com a produção {p}!")
                return False
            pred_set.update(pred)
    return True

