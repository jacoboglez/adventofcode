clear;clc

Sugar = [3, 0, 0, -3, 2];
Sprinkles = [-3, 3, 0, 0, 9];
Candy = [-1, 0, 4, 0, 1];
Chocolate = [0, 0, -2, 2, 8];

ingredients = [a; b; c; d];

max_score = 0;
max_score_500 = 0;
for ma = 1:100
%     fprintf('%d%%\n',ma)
    for mb = 1:100
        for mc = 1:100

            % Compute the last ingredient so it adds up to 100
            md = 100-ma-mb-mc;
            
            % If you have too many ingredients continue
            if md < 0
                continue
            end

            measures = [ma, mb, mc, md];

            score = prod( max(measures*ingredients(:,1:end-1), 0) );

            if score > max_score
                max_score = score;
            end

            cals = measures*ingredients(:,end);

            if (cals == 500) && (score > max_score_500)
                max_score_500 = score;
            end
        end
    end
end

fprintf('Part 1: %d\n',max_score)
fprintf('Part 2: %d\n',max_score_500)