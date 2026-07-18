-- Remove the empty chapter emitted for the HTML-only index.qmd in PDF builds.
-- Quarto books always process index.qmd; when its content is HTML-only,
-- Pandoc still receives an empty level-1 header and renders it as a blank
-- numbered PDF chapter. This filter drops only that generated empty header.

function Header(el)
  if FORMAT:match("latex")
    and el.level == 1
    and el.identifier == "section"
    and #el.content == 0 then
    return {}
  end
end
