<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output method="xml" indent="yes" encoding="UTF-8" doctype-system="./schemas/ead_sia.dtd"/>
    
    <!-- Supprime les espaces non voulues-->
    <xsl:strip-space elements="*"/>
    
    <xsl:template match="ead">
        <xsl:copy>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="eadheader">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="archdesc">
        <archdesc level="series">
            <xsl:apply-templates/>
        </archdesc>
    </xsl:template>
    
    <xsl:template match="did">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="accessrestrict">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="userestrict">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="acqinfo">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="bioghist">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="custodhist">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="arrangement">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="separatedmaterial">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="relatedmaterial">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="processinfo">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="controlaccess">
        <xsl:copy-of select="."/>
    </xsl:template>
    
    <xsl:template match="dsc">
        <xsl:copy>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="c">
        <xsl:copy>
            <xsl:copy-of select="@*"/>
            <xsl:apply-templates/>
        </xsl:copy>
    </xsl:template>
    
    <xsl:template match="c/scopecontent//item"><!-- On transforme les scopecontent en c de level subgrp -->
        <xsl:choose>
            <xsl:when test=".[not(@level='subgrp')]">
                <c level="subgrp">
                    <did>
                        <unittitle>
                            <xsl:choose><!-- Gestion des sous-parties -->
                                <xsl:when test="contains(./text(), ' :')"><!-- S'il y a deux points et donc plusieurs contenus -->
                                    <!-- Le titre contient la partie précédant les deux points -->
                                    <xsl:value-of select="substring-before(./text(), ' :')"/>
                                </xsl:when>
                                <xsl:otherwise><!-- S'il n'y a pas deux points et donc un seul contenu -->
                                    <xsl:choose><!-- Gestion des dates : on ne veut pas imprimer la date dans le titre -->
                                        <xsl:when test="contains(./text(), '(19')"><!-- Si le texte contient une date -->
                                            <xsl:variable name="title" select="substring-before(./text(), ' (19')"/>
                                            <xsl:value-of select="$title"/>
                                        </xsl:when>
                                        <xsl:otherwise><!-- Si le texte ne contient pas de date -->
                                            <xsl:value-of select="./text()"/>
                                        </xsl:otherwise>
                                    </xsl:choose>
                                </xsl:otherwise>
                            </xsl:choose>
                        </unittitle>
                        <xsl:choose><!-- Gestion des dates -->
                            <xsl:when test="contains(./text(), '(19')">
                                <xsl:variable name="date" select="substring-after(./text(), '(19')"/>
                                <xsl:variable name="date" select="replace($date, '\)', '')"/>
                                <xsl:variable name="date" select="replace($date, '\.', '')"/>
                                <xsl:variable name="date" select="concat('19', $date)"/>
                                <unitdate>
                                    <xsl:attribute name="normal">
                                        <xsl:value-of select="replace($date, '-', '/')"/>
                                    </xsl:attribute>
                                    <xsl:value-of select="$date"/>
                                </unitdate>
                            </xsl:when>
                        </xsl:choose>
                    </did>
                    <xsl:if test="contains(./text(), ' :')"><!-- S'il y a deux points et donc plusieurs contenus -->
                        <!-- On place le contenu en commentaire -->
                        <scopecontent>
                            <xsl:comment>
                                <xsl:text>Encoder le contenu</xsl:text>
                            </xsl:comment>
                            <p>    
                                <xsl:value-of select="substring-after(./text(), ' : ')"/>
                            </p>
                        </scopecontent>
                    </xsl:if>
                </c>
            </xsl:when>
            <xsl:otherwise>
                <xsl:copy-of select="."/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
    <xsl:template match="comment()">
        <xsl:copy/>
    </xsl:template>
    
    
    
</xsl:stylesheet>