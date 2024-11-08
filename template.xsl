<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html"/>

<!-- Page Template -->

<xsl:template match="page">
<html>
    <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>GLUG</title>
        <link rel="stylesheet" href="css/style.css"> </link>
    </head>

    <body>
        <div id="header-outer">
            <div id="header" class="banner-center">
                <img src="logo.svg" class="logo"/>
                <div id="nonlogo">
                <strong style="font-size:1.5em;"> GNU/Linux Users' Group</strong>
                <strong style="color:white; font-size: 0.9em;">Association for Computing Machinery</strong><br></br>
                <strong style="color:white; font-size: 0.9em;">University of Illinois Urbana-Champaign</strong>
                </div>
            </div>
        </div>

        <div id="navbar">
            <div class="banner-center">
                <a href="index.html">Home</a>
                <a href="https://github.com/gnulug">Git</a>
                <a href="links.html">Join Chat</a>
            </div>
        </div>

        <div id="content">
            <!-- Page content will be inserted here -->
            <xsl:apply-templates/>
        </div>
    </body>
</html>
</xsl:template>

<xsl:template match="page2">
<html>
    <b><xsl:value-of select="author"/></b>
    <em>(<xsl:value-of select="date"/>)</em>

    <xsl:value-of select="text()"/>
</html>
</xsl:template>


<!-- Wildcard Template -->
<!-- This is required so that tags not defined here (e.g. HTML) are rendered as is -->

<xsl:template match="node()|@*">
    <xsl:copy>
        <xsl:apply-templates select="node() | @*"/>
    </xsl:copy>
</xsl:template>

</xsl:stylesheet>
