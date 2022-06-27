<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">

<xsl:variable name="Paris">
    <xsl:text>Paris</xsl:text>
</xsl:variable>

<xsl:template match="/">
    <controlaccess>
        <xsl:apply-templates mode="dpt"/>
        <xsl:apply-templates mode="cmn"/>
        <xsl:apply-templates mode="mh_non-Paris"/>
        <xsl:apply-templates mode="mh_Paris"/>
    </controlaccess>
</xsl:template>

    <xsl:template match="@* | node()" mode="#all">
        <xsl:apply-templates mode="#current"/>
    </xsl:template>

<xsl:template match="departement[@id]" mode="dpt">
    <geogname>
        <xsl:attribute name="authfilenumber">
            <xsl:value-of select="./@id"/>
        </xsl:attribute>
        <xsl:attribute name="source">
            <xsl:text>FRAN_RI_005</xsl:text>
        </xsl:attribute>
        <xsl:value-of select="./nom/text()"/>
    </geogname>
</xsl:template>
    
    <xsl:template match="commune[@id]" mode="cmn">
        <geogname>
            <xsl:attribute name="authfilenumber">
                <xsl:value-of select="./@id"/>
            </xsl:attribute>
            <xsl:attribute name="source">
                <xsl:text>FRAN_RI_005</xsl:text>
            </xsl:attribute>
            <xsl:value-of select="./nom/text()"/>
        </geogname>
    </xsl:template>
    
    <xsl:template match="mh[preceding-sibling::nom/text()!=$Paris][@id]" mode="mh_non-Paris">
        <geogname>
            <xsl:variable name="NA">
                <xsl:text>NA</xsl:text>
            </xsl:variable>
            <xsl:if test="./@id!=$NA">
                <xsl:attribute name="authfilenumber">
                    <xsl:value-of select="./@id"/>
                </xsl:attribute>
                <xsl:attribute name="source">
                    <xsl:text>FRAN_RI_005</xsl:text>
                </xsl:attribute>
            </xsl:if>
            <xsl:value-of select="./text()"/>
        </geogname>
    </xsl:template>
    
    <xsl:template match="mh[preceding-sibling::nom/text()=$Paris][@id]" mode="mh_Paris">
        <geogname>
            <xsl:variable name="NA">
                <xsl:text>NA</xsl:text>
            </xsl:variable>
            <xsl:if test="./@id!=$NA">
            <xsl:attribute name="authfilenumber">
                <xsl:value-of select="./@id"/>
            </xsl:attribute>
            <xsl:attribute name="source">
                <xsl:text>FRAN_RI_026</xsl:text>
            </xsl:attribute>
            </xsl:if>
            <xsl:value-of select="./text()"/>
        </geogname>
    </xsl:template>

</xsl:stylesheet>