import math


def parse_pool(pool_line):
    return [token.strip().upper() for token in pool_line.split(",") if token.strip()]


def parse_student_id(id_line):
    return [int(token) for token in id_line.split()]


def build_weights(student_id_digits, target_length):
    if target_length <= 0:
        return []
    if len(student_id_digits) >= target_length:
        return student_id_digits[-target_length:]
    return list(student_id_digits)


def utility(gene, target, weights):
    total = 0
    n = max(len(gene), len(target))

    for i in range(n):
        w_i = weights[i] if i < len(weights) else 1
        gene_ascii = ord(gene[i]) if i < len(gene) else 0
        target_ascii = ord(target[i]) if i < len(target) else 0
        total += w_i * abs(gene_ascii - target_ascii)

    return -total


def minimax_alpha_beta(gene, remaining_pool, target, weights, is_max_turn, alpha, beta):
    if not remaining_pool:
        return gene, utility(gene, target, weights)

    if is_max_turn:
        best_score = -math.inf
        best_gene = ""

        for i, nucleotide in enumerate(remaining_pool):
            next_gene = gene + nucleotide
            next_pool = remaining_pool[:i] + remaining_pool[i + 1 :]
            candidate_gene, candidate_score = minimax_alpha_beta(
                next_gene, next_pool, target, weights, False, alpha, beta
            )

            if candidate_score > best_score:
                best_score = candidate_score
                best_gene = candidate_gene

            alpha = max(alpha, best_score)
            if beta <= alpha:
                break

        return best_gene, best_score

    best_score = math.inf
    best_gene = ""

    for i, nucleotide in enumerate(remaining_pool):
        next_gene = gene + nucleotide
        next_pool = remaining_pool[:i] + remaining_pool[i + 1 :]
        candidate_gene, candidate_score = minimax_alpha_beta(
            next_gene, next_pool, target, weights, True, alpha, beta
        )

        if candidate_score < best_score:
            best_score = candidate_score
            best_gene = candidate_gene

        beta = min(beta, best_score)
        if beta <= alpha:
            break

    return best_gene, best_score


def main():
    lines = []
    while len(lines) < 3:
        try:
            line = input().strip()
        except EOFError:
            break
        if line:
            lines.append(line)

    if len(lines) < 3:
        return

    pool = parse_pool(lines[0])
    target = lines[1].strip().upper()
    student_id_digits = parse_student_id(lines[2])
    weights = build_weights(student_id_digits, len(target))

    best_gene, best_score = minimax_alpha_beta(
        "", pool, target, weights, True, -math.inf, math.inf
    )

    print(f"Best gene sequence generated: {best_gene}")
    print(f"Utility score: {best_score}")


if __name__ == "__main__":
    main()



