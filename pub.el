;; This should be a symlink to the installed version like:
;; ~/.emacs.d/elpa/org-20140104/

(add-to-list 'load-path "~/org-pub/emacs.d/htmlize")
(add-to-list 'load-path "~/org-pub/emacs.d/org")

(require 'htmlize)
(require 'org)
(require 'org-publish)

(setq org-src-fontify-natively t)
(setq org-export-htmlize-output-type 'css)
(setq org-publish-project-alist
      
      `(("blog"
	 :components (
		      "blog-static"
		      "blog-log"
		      "blog-topics"
		      ))
	("blog-static"
	 :base-directory "~/org-pub"
	 :base-extension "css\\|js\\|png\\|org"
	 :publishing-directory "~/public_html/pub"
	 :recursive t
         :publishing-function org-publish-attachment)

	("blog-log"
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

	("blog-topics"
	 :base-extension "org"
	 :base-directory "~/org-pub/topics"
	 :publishing-directory "~/public_html/pub/topics"
	 :recursive t
         :publishing-function org-html-publish-to-html
	 ;:preparation-function org-mode-blog-prepare
         :export-with-tags nil
         :headline-levels 4
         :auto-sitemap t
         :sitemap-title "Sitemap"
         :section-numbers t
         :with-toc t
         :with-author t
         :with-creator t
         :html-doctype "html5"
         :html-preamble org-pub-preamble
         :html-postamble "<hr><div id='comments'></div>"
         :html-head  "<link rel=\"stylesheet\" href=\"/css/style.css\" type=\"text/css\"/>\n"
         :html-head-extra "<script async=\"true\" src=\"/js/juvia.js\"></script>
         <link rel=\"shortcut icon\" href=\"/img/steckerhalter.ico\">
         <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, maximum-scale=1\" />"
         :html-html5-fancy t
         :html-head-include-default-style t
	 )


        ))

(defun org-pub-preamble (options)
  "Returns HTML to use as the preamble"
  (let ((base-directory (plist-get options :base-directory)))
    (org-babel-with-temp-filebuffer (expand-file-name "../html/preamble.html" base-directory) (buffer-string))))
