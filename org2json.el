;; Export an org-mode document into JSON with minimal interference.
;;
;; Made by an elisp dummy with lots of help from the friendly org mailing list.
;;
;; http://lists.gnu.org/archive/html/emacs-orgmode/2013-12/msg00154.html
;;

(require 'json)


(defun org-json-straigten-tree (tree)
  "Null out circular references in the org-element TREE"
  (org-element-map tree (append org-element-all-elements
				org-element-all-objects '(plain-text))

    ;; the crux of this is to nullify references that turn the tree
    ;; into a Circular Object which the json module can't handle
    (lambda (x) 
      ;; guaranteed circluar
      (if (org-element-property :parent x)
	  (org-element-put-property x :parent "none"))
      ;; maybe circular if multiple structures accidently identical
      (if (org-element-property :structure x)
	  (org-element-put-property x :structure "none"))
      ))
  tree)

(defun org-json-tree-to-json-string (tree)
  "Return a JSON formatted string representing the given org-element tree"
  (json-encode (org-json-straigten-tree tree)))

(defun org-json-buffer-to-tree ()
  "Return org-element tree for current buffer"
  (org-element-parse-buffer 'object nil))

(defun org-json-buffer-to-json-string ()
  "Return a JSON formatted string representing the org-element tree from the current org buffer"
  (interactive)
  (let* ((tree (org-json-buffer-to-tree)))
    (org-json-tree-to-json-string tree)))

(defun org-json-buffer-to-json-file (&optional path)
  "Write a JSON file from the current org buffer"
  (interactive "Fwrite to JSON file: ")
  (let ((tree (org-json-straigten-tree
               (org-json-buffer-to-tree))))
    (with-temp-file path
      (insert (org-json-tree-to-json-string tree)))))

(defun org-json-dump-file (filename)
  "Dump org file to json"
  (progn
    (save-excursion
      (find-file filename)
      (princ (org-json-buffer-to-json-string 
	      (org-json-straigten-tree
	       (org-json-buffer-to-tree)))))))

(defun org2json (src tgt)
  "Convert source org file to json file"
  (progn
    (save-excursion
      (find-file src)
      (org-json-buffer-to-json-file tgt))))

(defun org-json-buffer-to-json-file-old (&optional path)
  "Write a JSON file from the current org buffer"
  (interactive "Fwrite to JSON file: ")
  (let* ((tree (org-element-parse-buffer 'object nil)))
    (org-element-map tree (append org-element-all-elements
				  org-element-all-objects '(plain-text))

      ;; the crux of this is to nullify references that turn the tree
      ;; into a Circular Object which the json module can't handle
      (lambda (x) 
	;; guaranteed circluar
        (if (org-element-property :parent x)
            (org-element-put-property x :parent "none"))
	;; maybe circular if multiple structures accidently identical
        (if (org-element-property :structure x)
            (org-element-put-property x :structure "none"))
        ))

    (with-temp-file path
      (insert (json-encode tree)))))

(defun org-json-buffer-to-sexp-file (&optional path)
  "Write a SEXP file from the current org buffer"
  (interactive "Fwrite to JSON file: ")
  (let* ((tree (org-element-parse-buffer 'object nil)))
    (org-element-map tree (append org-element-all-elements
				  org-element-all-objects '(plain-text))

      ;; the crux of this is to nullify references that turn the tree
      ;; into a Circular Object which the json module can't handle
      (lambda (x) 
	;; guaranteed circluar
        (if (org-element-property :parent x)
            (org-element-put-property x :parent "none"))
	;; maybe circular if multiple structures accidently identical
        (if (org-element-property :structure x)
            (org-element-put-property x :structure "none"))
        ))

    (with-temp-file path
      (insert (prin1-to-string tree)))))


(require 'org-element)
(defun org-json-schema-to-json-file (&optional path)
  "Write a org-element schema to JSON file"
  (interactive "Fwrite to JSON file: ")
    (with-temp-file path
      (insert "{\n")
      (insert (concat "\"all-elements\":" (json-encode org-element-all-elements)))

      (insert ",\n")
      (insert (concat "\"greater-elements\":" (json-encode org-element-greater-elements)))

      (insert ",\n")
      (insert (concat "\"all-successors\":" (json-encode org-element-all-successors)))

      (insert ",\n")
      (insert (concat "\"successor-alist\":" (json-encode org-element-object-successor-alist)))

      (insert ",\n")
      (insert (concat "\"all-objects\":" (json-encode org-element-all-objects)))

      (insert ",\n")
      (insert (concat "\"recursive-objects\":" (json-encode org-element-recursive-objects)))

      (insert ",\n")
      (insert (concat "\"affiliated-keywords\":" (json-encode org-element-affiliated-keywords)))

      (insert ",\n")
      (insert (concat "\"document-properties\":" (json-encode org-element-document-properties)))

      (insert ",\n")
      (insert (concat "\"object-restrictions\":" (json-encode org-element-object-restrictions)))

      (insert "\n")
      (insert "}\n")))
;(org-json-schema-to-json-file "schema.json")
	      
		  
(provide 'org-json)
