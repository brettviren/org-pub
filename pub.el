(add-to-list 'load-path "~/org-pub/emacs.d/htmlize")
(add-to-list 'load-path "~/org-pub/emacs.d/org")

(require 'htmlize)
(require 'org)
;(require 'org-publish)

(org-babel-do-load-languages
 'org-babel-load-languages
 '((python . t)))


(defun bv-pub-postamble (options)
  "Returns HTML to use as the postamble"
  (concat "<b/><hr/><b/><a href=\"" (plist-get options :input-buffer) "\">Org source</a>"))
	  

(setq org-src-fontify-natively t)
(setq org-export-htmlize-output-type 'css)
;(setq org-publish-sitemap-file-entry-format "%t  (%d)")
(setq org-publish-project-alist
      
      `(("pub-all"
	 :components (
		      "pub-static"
;		      "pub-log"
		      "pub-topics"
		      ))
	("pub-static"
	 :base-directory "~/org-pub"
	 :base-extension "css\\|js\\|png\\|org"
	 :publishing-directory "~/public_html/pub"
	 :recursive t
	 :sitemap-sort-files anti-chronologically
         :publishing-function org-publish-attachment)


	("pub-log"
	 :base-extension "org"
	 :base-directory "~/org-pub/log"
	 :publishing-directory "~/public_html/pub/log"
	 :recursive t
         :publishing-function org-html-publish-to-html
	 ;:preparation-function org-mode-blog-prepare
         :export-with-tags nil
         :headline-levels 4
         :auto-sitemap t
         :sitemap-title "Sitemap"
	 :sitemap-sort-files anti-chronologically
         :section-numbers nil
         :with-toc nil
         :with-author nil
         :with-creator nil
         :html-doctype "html5"
         :html-preamble  org-pub-preamble
         :html-postamble "<hr><div id='comments'></div>"
         :html-head  "<link rel=\"stylesheet\" href=\"/css/style.css\" type=\"text/css\"/>\n"
         :html-head-extra "<script async=\"true\" src=\"/js/juvia.js\"></script>
         <link rel=\"shortcut icon\" href=\"/img/steckerhalter.ico\">
         <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\" />"
         :html-html5-fancy t
         :html-head-include-default-style t
	 )

	("pub-topics"
	 :base-extension "org"
	 :base-directory "~/org-pub/topics"
	 :publishing-directory "~/public_html/pub/topics"
	 :recursive t
         :publishing-function org-html-publish-to-html
	 ;:preparation-function org-mode-blog-prepare
         :export-with-tags nil
	 :export-creator-info nil
         :export-author-info nil
         :headline-levels 4
         :auto-sitemap t
         :sitemap-title "Sitemap"
	 :sitemap-style list
	 :sitemap-sort-files anti-chronologically
         :section-numbers t
         :with-toc nil
         :with-author t
         :with-creator t
	 :with-tags t
	 :exclude-tags ("noexport" "todo")
         :html-doctype "html5"
         :html-preamble t
         :html-postamble bv-pub-postamble
         :html-head  "<link rel=\"stylesheet\" href=\"/css/style.css\" type=\"text/css\"/>\n"
         :html-head-extra "<script async=\"true\" src=\"/js/juvia.js\"></script>
         <link rel=\"shortcut icon\" href=\"/img/steckerhalter.ico\">
         <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\" />"
         :html-html5-fancy t
         :html-head-include-default-style t
	 )
        ))

;(setq org-export-html-postamble-format "
;<b>
;<hr>
;<p class=\"postamble\">Last Updated %d. Created by %c</p>
;THIS IS THE END.
;")


(defun org-pub-preamble (options)
  "Returns HTML to use as the preamble"
  (let ((base-directory (plist-get options :base-directory)))
    (org-babel-with-temp-filebuffer (expand-file-name "../html/preamble.html" base-directory) (buffer-string))))


(defun org-pub-postamble (options)
  "Returns HTML to use as the postamble"
  buffer-file-name)
