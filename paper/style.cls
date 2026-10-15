
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{custom}
\LoadClassWithOptions{article}

% Layout %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage[top=2.1cm, bottom=2.cm, left=2.2cm, right=2.2cm, columnsep=0.75cm]{geometry}
\RequirePackage{microtype}
\RequirePackage{placeins}
\RequirePackage{hyphenat}
\RequirePackage{setspace}
\RequirePackage{parskip}
\RequirePackage[latin, english]{babel}
\RequirePackage{etoolbox}
\RequirePackage{pifont}

% Graphics & Tables %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage{graphicx}
\RequirePackage{subcaption}
\RequirePackage{booktabs}
\RequirePackage{nicematrix}
\RequirePackage{multirow}
\RequirePackage{bm}

% Modern Color Palette %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% \RequirePackage[many]{tcolorbox}
\RequirePackage[many]{tcolorbox}
\tcbuselibrary{skins} % This provides "enhanced"
% \tcbuselibrary{breaks}
\RequirePackage{xcolor}

\definecolor{accent-bright}{HTML}{4440C6}      % Deep accent indigo for borders/headers ($accent-bright)
\definecolor{accent}{HTML}{6B67EE}  % Primary purple for links/captions ($purple-color)
\definecolor{bg}{HTML}{F9F9FE}       % Site background ($bg-deep)
\definecolor{slatetext}{HTML}{1a1a2e}    % Dark navy body text ($black-color / $grey-900)
\definecolor{accent-brightlight}{HTML}{D4D3FA} % Light purple fill ($accent-light)
\definecolor{linecolor}{HTML}{F0F0F8}    % Surface tone for horizontal rule ($bg-surface)
% References %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage{hyperref}
\RequirePackage[noabbrev,nameinlink]{cleveref}
\hypersetup{
  colorlinks,
  linkcolor=accent-bright,    % Changed from forestlink
  citecolor=accent,    % Changed from forestlink
  urlcolor=accent  % Changed from forestlink
}

\RequirePackage[round,authoryear]{natbib}
\def\bibfont{\small}

% Typography & Sectioning %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\RequirePackage{titlesec}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage{inconsolata} 

% Section Styles: Using Slate for a softer feel than pure black
\titleformat*{\section}{\Large\sffamily\bfseries\color{slatetext}}
\titleformat*{\subsection}{\large\sffamily\bfseries\color{slatetext}}
\titleformat*{\subsubsection}{\normalsize\sffamily\bfseries\color{slatetext}}
\titleformat*{\paragraph}{\sffamily\bfseries\color{slatetext}}

%\DeclareTextFontCommand{\textbf}{\bfseries\sffamily}

% Captions
\RequirePackage{caption}
\DeclareCaptionLabelSeparator{custom}{ }
\DeclareCaptionFormat{custom}{{\sffamily\textbf{\color{accent-bright}#1 #2}} #3}
\captionsetup{
  format=custom,
  labelsep=custom,
  font={small,it},
  justification=justified,
  singlelinecheck=true
}
% Authors & Affiliations Logic %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand\addtolistcustom[5][]{
  \begingroup
    \if\relax#3\relax\def\sep{}\else\def\sep{#5}\fi
    \let\protect\@unexpandable@protect 
    \xdef#3{\expandafter{#3}\sep #4[#1]{#2}}%
  \endgroup
}

\newcommand\authorlist{}
\newcommand\authorformat[2][]{{ \bfseries \color{slatetext} #2$^{#1}$}}
\renewcommand\author[2][]{\addtolistcustom[#1]{#2}{\authorlist}{\authorformat}{, }}

\newcommand\affiliationlist{}
\newcommand\affiliationformat[2][]{{\small\itshape $^{#1}$#2}}
\newcommand\affiliation[2][]{\addtolistcustom[#1]{#2}{\affiliationlist}{\affiliationformat}{, }}

\newcommand\contributionlist{}
\newcommand\contributionformat[2][]{{\small $^{#1}$#2}}
\newcommand\contribution[2][]{\addtolistcustom[#1]{#2}{\contributionlist}{\contributionformat}{, }}

\newcommand\metadatalist{}
\newcommand\metadataformat[2][]{{\small {\sffamily \bfseries \color{accent-bright} #1:} #2}}
\newcommand\metadata[2][]{\addtolistcustom[#1]{#2}{\metadatalist}{\metadataformat}{\par}}

\renewcommand{\abstract}[1]{\def\abstractlist{{\small\setstretch{1.2}#1}}}
\newcommand{\email}[1]{\href{mailto:#1}{\texttt{#1}}}

\renewcommand\date[1]{\metadata[Date]{#1}}
\newcommand\correspondence[1]{\metadata[Correspondence]{#1}}
\renewcommand{\title}[1]{\newcommand{\titlelist}{{\huge\sffamily\bfseries\color{slatetext} #1}}}

% Updated Titlebox with more presence
\newcommand{\mymaketitle}{%
  \tcbset{
    enhanced,
    boxrule=1.0pt,
    colframe=accent-bright!30!accent,
    colback=bg!50!white,
    arc=8pt,
    left=0.8cm, right=0.8cm, top=0.6cm, bottom=0.5cm,
    % shadow={2mm}{-2mm}{0mm}{black!10}
  }
  \begin{tcolorbox}
    \setlength{\parindent}{0cm}
    \begin{center}
      \nohyphens
      {\setstretch{1.3}\titlelist\par}
      \vspace{0.4cm}
      {\authorlist\par}
      \vspace{0.2cm}
      {\affiliationlist\par}
      {\contributionlist\par}
    \end{center}
    \vspace{0.1cm}
    {\centering \textcolor{accent-bright!30}{\rule{0.6\textwidth}{1pt}} \par}
    \vspace{0.2cm}
    {\sffamily\bfseries\color{accent-bright} Abstract.} \abstractlist\par
  \end{tcolorbox}
  \FloatBarrier
}

% Fix for the Appendix command
\newcommand{\beginappendix}{%
  \clearpage
  \appendix
  \section*{\huge\sffamily\bfseries\color{accent-bright} Appendix}
  \addcontentsline{toc}{section}{Appendix}
}

\renewcommand{\maketitle}{\mymaketitle}
\RequirePackage{enumitem}

