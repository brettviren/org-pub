(add-to-list 'load-path "~/org-pub/emacs.d/htmlize")
(add-to-list 'load-path "~/org-pub/emacs.d/org")
;(add-to-list 'load-path "~/org-pub/emacs.d/ox-gfm")


(require 'htmlize)
(require 'org)


;; (setq org-latex-pdf-process
;;       '("pdflatex --shell-escape -interaction nonstopmode -output-directory %o %f" 
;; 	"pdflatex --shell-escape -interaction nonstopmode -output-directory %o %f" 
;; 	"pdflatex --shell-escape -interaction nonstopmode -output-directory %o %f"))

;; (org-babel-do-load-languages
;;  'org-babel-load-languages
;;  '(
;;    (sh . t)
;;    (python . t)
;;    (ditaa . t)
;;    (dot . t)
;;    (sqlite . t)
;;    ))
;; (setq org-confirm-babel-evaluate nil)
