(defun org2body (src tgt)
  "Dump body of org file to HTML"
  (progn
    (save-excursion
      (find-file src)
      (org-html-export-as-html nil nil nil t)
      (with-current-buffer "*Org HTML Export*"
	(write-file tgt)))))
